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
from models.classification import Classification as Models
import conf.proto.test_proto.test_pb2 as pb2
import conf.proto.test_proto.test_pb2_grpc as pb2_grpc
from queue import Queue

setproctitle.setproctitle("Server")
_ONE_DAY_IN_SECONDS = 60 * 60


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
        # print(request.log)
        for i in range(len(request.log)):
            request.log[i] = request.log[i] + " " + str(mytime.get_latency_ms(request.timestamp)) + " ms "
        # for log in request.log:
        #     log = log + " "+ str(mytime.get_latency_ms(timestamp))+" ms "
        self.queue.put(request)
        self.arrive_t.put(mytime.get_timestamp())  # 获取当前时间戳
        # print(request.log)
        # print(request.index)
        return pb2.F2S_Response(flag=True)


class Server:
    def __init__(self, port, aimport, feport, model_name, batch=1):
        """

        :param port: server port
        :param aimport: client port
        :param feport:  frontend port
        :param batch:   server process batch
        """
        self.model_name = model_name
        self.arrive_t = Queue()
        self.port = port
        self.model = None
        self.batch = batch
        self.feport = feport
        self.aim_port = aimport
        self.queue = Queue()
        self.send_q = Queue()

        # send server config to frontend
        target_port = 'localhost:' + str(self.feport)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.SetupStub(channel)
            msg_send = pb2.Setup_Request(port=str(self.port), batch=self.batch)
            res = stub.Setup_getmsg(msg_send)

    def __load_model(self):
        # 模型加载时间为 4s
        s = time.time()
        time.sleep(0.5)
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
            delayMs(40)
            time.sleep(latency / 1000)
        elif batchsize == 2:
            # 2 40
            s = time.time()
            delayMs(40)  # 延迟40ms
            print("batchsize = 2")
            latency = (time.time() - s) * 1000
        elif batchsize == 4:
            # 4 21
            latency = random.gauss(21, 1)
            time.sleep(latency / 1000)
        elif batchsize == 8:
            # 8 34
            latency = random.gauss(34, 1)
            time.sleep(latency / 1000)

        return latency

    def __model(self):
        # loading model
        self.__load_model()

        while True:
            # prepare image data
            reqs = self.queue.get()
            # size = reqs.size
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
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
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
        target_port = 'localhost:' + str(self.aim_port)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.S2CStub(channel)
            msg_send = pb2.S2C_Request(res=res, index=request_id, log=log, timestamp=mytime.get_timestamp())
            st = time.time()
            stub.S2C_getmsg(msg_send)
            print("sever to client{:.3f}ms".format((time.time() - st) * 1000))

    def run(self):
        t1 = threading.Thread(target=self.__server)
        t2 = threading.Thread(target=self.__model)
        # t3 = threading.Thread(target=self.send)
        t1.start()
        t2.start()
        # t3.start()


def main():
    s = Server(port=50002, aimport=50000, feport=50001, model_name="VGG", batch=2)
    # s2 = Server(port=50003, aimport=50000, feport=50001, model_name="VGG", batch=2)
    # s2.run()
    s.run()


if __name__ == '__main__':
    main()
