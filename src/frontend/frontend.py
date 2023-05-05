#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 11:24 AM
# @Author  : Agonsle
# @Site    : 
# @File    : frontend.py
# @Software: PyCharm
"""
    schedule frontend:
    1. collect img_data from clients
    2. preprocess img_data (resize & normalization)
    3. distribute datas to different worker

"""
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


class F_Request:

    def __init__(self, img, request_id):
        self.img = img
        self.request_id = request_id


class C2F(pb2_grpc.C2FServicer):
    """
        grpc client to frontend
    """

    def __init__(self, queue):
        self.queue = queue

    def C2F_getmsg(self, request, context):
        self.queue.put(request)
        return pb2.C2F_Response(flag=True)


class Setup(pb2_grpc.SetupServicer):
    """
        register workload config in frontend
    """

    def __init__(self, dic, server_port, list_q):
        self.dic = dic
        self.list_q = list_q
        self.server_port = server_port

    def Setup_getmsg(self, request, context):
        self.dic[request.port] = request.batch
        self.server_port.append(request.port)
        self.list_q.append([])
        print("Frontend target server config is {}".format(self.dic))
        # print(self.server_port)
        return pb2.S2C_Response(flag=True)


class Frontend:
    def __init__(self, port, height=224, width=224,policy="BA"):
        """

        :param port: Frontend ip
        :param height: preprocess img height
        :param width: preprocess img width
        """
        self.policy = policy
        self.server_port = []
        self.config = {}  # port-->batch对应关系
        self.port = port
        self.list_q = []
        self.recv_q = Queue()
        self.target = 0
        self.send_q = Queue()
        self.width = width
        self.height = height

    def __server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        pb2_grpc.add_C2FServicer_to_server(C2F(self.recv_q), server)
        pb2_grpc.add_SetupServicer_to_server(Setup(self.config, self.server_port, self.list_q), server)
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

    def __preprocess(self, req):
        request_id = req.request_id # 请求序号
        h = req.image.height
        w = req.image.width
        img_bytes = req.image.byte_image
        # pic resize
        img = np.frombuffer(img_bytes, dtype=np.uint8)
        img = img.reshape(h, w, 3)
        img = cv2.resize(img, (self.width, self.height), interpolation=cv2.INTER_AREA)
        # pic to bytes
        img = img.tobytes()

        return img

    def __data_save(self):
        print("data save is running -- ")
        while True:
            while not self.recv_q.empty():
                req = self.recv_q.get()
                self.send_q.put(self.__preprocess(req))

    def __schedule(self):
        if self.policy == "RR":
            self.__RoundRobin()
        if self.policy == "BA":
            self.__BatchAware()

    def __RoundRobin(self):
        index = 0
        request_id = 1
        print("--- Scheduling policy RoundRobin ---")
        while True:
            while not self.send_q.empty():
                self.list_q[index].append(self.send_q.get())
                print(" index {} len {}".format(index, len(self.list_q[index])))
                if len(self.list_q[index]) == self.config[self.server_port[index]]:
                    aim_port = self.server_port[index]
                    bytes_img = self.list_q[index]
                    t1 = threading.Thread(target=self.__send_req,
                                          kwargs={'aim_port': self.server_port[index], 'request_id': request_id,
                                                  'bytes_img': bytes_img})
                    t1.start()
                    t1.join()
                    self.list_q[index].clear()
                    request_id = request_id + 1
                index = (index + 1) % len(self.config)

    def __BatchAware(self):
        print("--- Scheduling policy BatchAware ---")
        index = 0
        request_id = 1
        while True:
            while not self.send_q.empty():
                port = self.server_port[index]
                batch = self.config[port]
                while batch:
                    self.list_q[index].append(self.send_q.get())
                    batch = batch - 1

                t1 = threading.Thread(target=self.__send_req,
                                      kwargs={'aim_port': self.server_port[index], 'request_id': request_id,
                                              'bytes_img': self.list_q[index]})
                t1.start()
                t1.join()
                self.list_q[index].clear()
                request_id = request_id + 1
                index = (index + 1) % len(self.config)

    def __send_req(self, aim_port, request_id, bytes_img):
        target_port = 'localhost:' + str(aim_port)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.F2SStub(channel)
            msg_send = pb2.F2S_Request(request_id=request_id, size=self.width, image=bytes_img)
            response = stub.F2S_getmsg(msg_send)

    def run(self):

        t1 = threading.Thread(target=self.__server)  # 启动服务端
        t2 = threading.Thread(target=self.__data_save)  # 启动转发端
        t3 = threading.Thread(target=self.__schedule)  # 启动发送端
        t1.start()
        t2.start()
        t3.start()


def main():
    s = Frontend(port=50001,policy="RR")
    s.run()


if __name__ == '__main__':
    main()
