#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 1:53 PM
# @Author  : Agonsle
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import setproctitle
import random
import copy
import threading
import time
import grpc
from concurrent import futures
import numpy as np
import lib.mstime as mytime
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
import conf.proto.test_proto.test_pb2 as pb2
import conf.proto.test_proto.test_pb2_grpc as pb2_grpc
from queue import Queue

setproctitle.setproctitle("Server")
_ONE_DAY_IN_SECONDS = 60 * 60
_MS_TO_S = 0.001


class WorkerProfile:
    def __init__(self):
        self.drop_rate = 0
        self.drop_num = 0
        self.reci_req_num = 0
        self.throughput = 0


class Request2C:

    def __init__(self, res, log, request_id):
        self.res = res
        self.log = log
        self.request_id = request_id


class F2S(pb2_grpc.F2SServicer):

    def __init__(self, queue, arrive_t):
        self.queue = queue
        self.arrive_t = arrive_t

    def F2S_getmsg(self, request, context):
        for i in range(len(request.frontendmessage)):
            request.frontendmessage[i].log = request.frontendmessage[i].log + " " + str(
                mytime.get_latency_ms(request.frontendmessage[i].timestamp[-1])) + " ms "
            request.frontendmessage[i].timestamp.append(mytime.get_timestamp())
        self.flag = True
        self.queue.put(request.frontendmessage)
        return pb2.F2S_Response(flag=True)


class Server:
    """
    Worker:
        step1:先启动worker server
            - 用于接受Frontend发送过来的请求
            - 向Frontend发送请求，表明worker的配置
        step2:处理请求
        step3:向client发送请求
        step4:向Manage发送worker实时的吞吐量
    """
    def __init__(self, port, aimport, feport, model_name, profile,slo, batch=1):
        """

        :param port: server port
        :param aimport: client port
        :param feport:  frontend port
        :param batch:   server process batch
        """
        self.model_name = model_name  # 所使用的模型名称
        self.slo = slo  # SLOs 70ms
        self.arrive_t = Queue()  # 到达队列
        self.port = port  #
        self.worker_profile = WorkerProfile()
        self.model = None  # server加载何种模型
        self.profile = profile  # 模型的配置 batchsize -> duration(ms)
        self.batch = batch
        self.feport = feport
        self.aim_port = aimport
        self.queue = Queue()
        self.send_q = Queue()
        self.stub = None

        try:
            for key in self.profile:
                if self.profile[key] * 2 < self.slo:
                    self.batch = key  # 根据SLOs选择perferbatch
                else:
                    break
            print("prefer batch {}".format(self.batch))
        except:
            pass




        target_port = 'localhost:' + str(self.aim_port)
        channel = grpc.insecure_channel(target_port)
        self.stub = pb2_grpc.S2CStub(channel)

    def __deamon(self):
        while True:
            history_num = self.worker_profile.reci_req_num
            history_drop = self.worker_profile.drop_num
            time.sleep(1)
            diff_num = self.worker_profile.reci_req_num - history_num
            diff_drop = self.worker_profile.drop_num - history_drop
            self.worker_profile.throughput = diff_num
            if diff_num == 0:
                self.worker_profile.drop_rate = 0
            else:
                self.worker_profile.drop_rate = diff_drop / (diff_num * 1000 * _MS_TO_S)
            print(
                "server port{}, throughput is {} drop rate is {}".format(self.port, self.worker_profile.throughput,
                                                                         self.worker_profile.drop_rate))

    def __load_model(self):
        # 模型加载时间为 4s
        s = time.time()
        # time.sleep(0.5)
        print("模型加载完成，用时 {:.3f}s".format(time.time() - s))

    def __data_parse(self, bytes_img, size):
        img = np.frombuffer(bytes_img, dtype=np.uint8)
        img = img.reshape(size, size, 3)
        return img

    def __parse_batch(self, reqs, size):
        batch = []
        for req in reqs:
            img = np.frombuffer(req, dtype=np.uint8)
            img = img.reshape(size, size, 3)
            img = img_to_array(img)
            batch.append(img)

        return tf.convert_to_tensor(batch, dtype=tf.float32)

    def __inference(self, batchsize):
        latency = 0
        if batchsize == 1:
            # 1 25
            time.sleep(25 * _MS_TO_S)
        elif batchsize == 2:
            # 2 40
            time.sleep(40 * _MS_TO_S)  # 延迟40ms
        elif batchsize == 4:
            # 4 21
            pass
        elif batchsize == 8:
            # 8 34
            pass

        return latency

    def batch_check(self, reqs):
        """
        检测batch是否超时
        :return:
        """
        checked_reqs = []
        _batch = len(reqs)  # prefer batch
        self.worker_profile.reci_req_num = self.worker_profile.reci_req_num + _batch
        for r in reqs:
            if mytime.get_latency_ms(r.timestamp[0]) + self.profile[_batch] < self.slo:
                checked_reqs.append(r)
            else:
                _batch = _batch - 1
                self.worker_profile.drop_num = self.worker_profile.drop_num + 1  # drop ++

        return checked_reqs, _batch

    def __model(self):
        # loading model
        self.__load_model()

        while True:
            req = self.queue.get()
            # 合理性检查，返回修改后的_batch和req列表

            reqs, _batch = self.batch_check(req)
            if _batch > 0:
                self.__inference(_batch)
                res_list = []

                for r in reqs:
                    c = pb2.S2C_Request.ServerMessage()
                    c.res = "res"
                    c.index = r.id
                    c.log = r.log
                    for t in r.timestamp:
                        c.timestamp.append(t)
                    res_list.append(c)

                self.send_q.put(res_list)

    def __server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
        pb2_grpc.add_F2SServicer_to_server(F2S(self.queue, self.arrive_t), server)
        port = '[::]:' + str(self.port)
        server.add_insecure_port(port)
        server.start()

        target_port = 'localhost:' + str(self.feport)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.SetupStub(channel)
            msg_send = pb2.Setup_Request(port=str(self.port), batch=self.batch)
            response = stub.Setup_getmsg(msg_send)
            self.slo = response.slo

        try:
            while True:
                print("server is running")
                time.sleep(_ONE_DAY_IN_SECONDS)
                print("server is over")
        except KeyboardInterrupt:
            server.stop(0)

    def send(self):
        while True:
            req = self.send_q.get()

            self.__send_data(data=req)

    def __send_data(self, data):
        for i in range(len(data)):
            data[i].log = data[i].log + " " + str(
                mytime.get_latency_ms(data[i].timestamp[-1])) + " ms "
            data[i].timestamp.append(mytime.get_timestamp())
        msg_send = pb2.S2C_Request(request_id=1, servermessage=data)
        self.stub.S2C_getmsg(msg_send)

    def _Manage(self):
        # 先与Manage相连接
        target_port = 'localhost:' + str(40000)
        channel = grpc.insecure_channel(target_port)
        stub = pb2_grpc.S2DStub(channel)
        while True:
            msg_send = pb2.S2D_Request(throughput=int(self.worker_profile.throughput),
                                       max_throughput=int(self.profile[self.batch]),
                                       port=str(self.port))  # 把当前throughput的信息发送给Manager
            res = stub.S2D_getmsg(msg_send)
            time.sleep(1)

        pass

    def run(self):
        t1 = threading.Thread(target=self.__server)
        t2 = threading.Thread(target=self.__model)
        t3 = threading.Thread(target=self.send)
        t4 = threading.Thread(target=self.__deamon)
        t6 = threading.Thread(target=self._Manage)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t6.start()


def main():
    profile = {1: 25, 2: 40}
    s = Server(port=50002, aimport=50000, feport=50001, model_name="VGG", batch=2, profile=profile,slo=100)
    s2 = Server(port=50003, aimport=50000, feport=50001, model_name="VGG", batch=2, profile=profile,slo =100)
    s2.run()
    s.run()


if __name__ == '__main__':
    main()
