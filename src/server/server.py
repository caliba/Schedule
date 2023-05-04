#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 9:40 AM
# @Author  : Agonsle
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import random
import threading
import time
import grpc
from concurrent import futures
import numpy as np
import cv2  # BGR
import math

import conf.proto.msg_proto.msg_pb2 as pb2
import conf.proto.msg_proto.msg_pb2_grpc as pb2_grpc
from queue import Queue

_ONE_DAY_IN_SECONDS = 60 * 60


class F2S(pb2_grpc.F2SServicer):

    def __init__(self, queue):
        self.queue = queue

    def F2S_getmsg(self, request, context):
        self.queue.put(request)
        return pb2.F2S_Response(flag=True)


class Server:
    def __init__(self, port, aimport, feport, batch=1):
        """

        :param port: server port
        :param aimport: client port
        :param feport:  frontend port
        :param batch:   server process batch
        """
        self.port = port
        self.batch = batch
        self.feport = feport
        self.aim_port = aimport
        self.queue = Queue()

        # send server config to frontend
        target_port = 'localhost:' + str(self.feport)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.SetupStub(channel)
            msg_send = pb2.Setup_Request(port=str(self.port), batch=2)
            res = stub.Setup_getmsg(msg_send)

    def __data_parse(self, bytes_img, size):
        img = np.frombuffer(bytes_img, dtype=np.uint8)
        img = img.reshape(size, size, 3)
        return img

    def img_process(self):
        print("img_process is running ------")
        while True:
            while not self.queue.empty():
                reqs = self.queue.get()
                size = reqs.size
                res_list = []
                for req in reqs.image:
                    # preprocess data
                    img = self.__data_parse(req, size)
                    # model exec
                    self.__data_process()
                    res_list.append('res1')

                self.__send_data(res_list)
                # t = threading.Thread(target=self.__send_data)
                # t.start()

    def __data_process(self):
        t_sleep = random.uniform(5, 8)
        print('model process {} ms '.format(t_sleep))
        time.sleep(t_sleep / 1000)

    def start_server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        pb2_grpc.add_F2SServicer_to_server(F2S(self.queue), server)
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

    def __send_data(self, res):
        print("send server is running -- ")
        target_port = 'localhost:' + str(self.aim_port)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.S2CStub(channel)
            msg_send = pb2.S2C_Request(res=res)
            stub.S2C_getmsg(msg_send)

    def run(self):
        t1 = threading.Thread(target=self.start_server)
        t2 = threading.Thread(target=self.img_process)
        t1.start()
        t2.start()


def main():
    s = Server(port=50002, aimport=50000, feport=50001)
    s2 = Server(port=50003,aimport=50000,feport=50001)
    s2.run()
    s.run()


if __name__ == '__main__':
    main()
