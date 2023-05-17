#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 1:53 PM
# @Author  : Agonsle
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import setproctitle
import random
import threading
import time
import grpc
from concurrent import futures
import numpy as np
import lib.mstime as mytime
from tensorflow import keras
from lib.mstime import delayMs as delayMs
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
import conf.proto.test_proto.test_pb2 as pb2
import conf.proto.test_proto.test_pb2_grpc as pb2_grpc
from queue import Queue

setproctitle.setproctitle("Server")
_ONE_DAY_IN_SECONDS = 60 * 60
_MS_TO_S = 0.001


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
        for i in range(len(request.log)):
            request.log[i] = request.log[i] + " " + str(mytime.get_latency_ms(request.timestamp)) + " ms "
        self.queue.put(request)
        self.arrive_t.put(mytime.get_timestamp())  # 获取当前时间戳
        return pb2.F2S_Response(flag=True)


class Server:
    def __init__(self, port, aimport, feport, model_name, profile, batch=1):
        """

        :param port: server port
        :param aimport: client port
        :param feport:  frontend port
        :param batch:   server process batch
        """
        self.model_name = model_name  # 所使用的模型名称
        self.SLO = 70 # SLOs 70ms
        self.arrive_t = Queue()  # 到达队列
        self.port = port  #
        self.model = None # server加载何种模型
        self.profile = profile # 模型的配置 batchsize -> duration(ms)
        self.batch = batch
        self.feport = feport
        self.aim_port = aimport
        self.queue = Queue()
        self.send_q = Queue()
        self.stub = None

        # send server config to frontend
        target_port = 'localhost:' + str(self.feport)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.SetupStub(channel)
            msg_send = pb2.Setup_Request(port=str(self.port), batch=self.batch)
            stub.Setup_getmsg(msg_send)
        #
        target_port = 'localhost:' + str(self.aim_port)
        channel = grpc.insecure_channel(target_port)
        self.stub = pb2_grpc.S2CStub(channel)

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
            # 1 15
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

    def __model(self):
        # loading model
        self.__load_model()

        while True:
            # prepare image data
            reqs = self.queue.get()
            # 合理性检查
            _batch = len(reqs.index) # prefer batch
            for r in reqs.send_time:
                tmp = mytime.get_latency_ms(r)
                if tmp + self.profile[_batch] < self.SLO:
                    print("Time Out")
                    _batch = _batch - 1

            request_id = reqs.index
            res_list = []
            # batch = self.__parse_batch(reqs.image, size) # 数据预处理
            # model inference
            latency = self.__inference(len(reqs.index))
            for i in reqs.index:
                res_list.append("请求" + str(i))
            print("Port {}: message lens {} spend time {:.3f}ms".format(self.port, len(reqs.index), latency))
            arrive_time = self.arrive_t.get()
            for i in range(len(reqs.log)):
                reqs.log[i] = reqs.log[i] + str(mytime.get_latency_ms(arrive_time)) + " ms "

            r = Request2C(res=res_list, request_id=request_id, log=reqs.log)
            self.send_q.put(r)

    def __server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
        pb2_grpc.add_F2SServicer_to_server(F2S(self.queue, self.arrive_t), server)
        port = '[::]:' + str(self.port)
        server.add_insecure_port(port)
        server.start()

        try:
            while True:
                print("server is running")
                time.sleep(_ONE_DAY_IN_SECONDS)
                print("server is over")
        except KeyboardInterrupt:
            server.stop(0)

    def test(self):
        res = ["test1", "test2"]
        index = [1, 2]
        log = ["request_id 91 1.558ms  23.225ms  1.457 ms 40.16 ms  21.156 ms",
               "request_id 91 1.558ms  23.225ms  1.457 ms 40.16 ms  21.156 ms"]
        for i in range(6):
            self.__send_data(res, index, log)

    def send(self):
        while True:
            req = self.send_q.get()

            self.__send_data(res=req.res, request_id=req.request_id, log=req.log)

    def __send_data(self, res, request_id, log):
        msg_send = pb2.S2C_Request(res=res, index=request_id, log=log, timestamp=mytime.get_timestamp())
        self.stub.S2C_getmsg(msg_send)

    def run(self):
        t1 = threading.Thread(target=self.__server)
        t2 = threading.Thread(target=self.__model)
        t3 = threading.Thread(target=self.send)
        t1.start()
        t2.start()
        t3.start()


def main():
    profile = {1: 25, 2: 40}
    s = Server(port=50002, aimport=50000, feport=50001, model_name="VGG", batch=2, profile=profile)
    s2 = Server(port=50003, aimport=50000, feport=50001, model_name="VGG", batch=2, profile=profile)
    s2.run()
    s.run()


if __name__ == '__main__':
    main()
