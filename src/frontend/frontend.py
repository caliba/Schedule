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
from lib.Schedule import Schedule
_ONE_DAY_IN_SECONDS = 60 * 60


class C2F(pb2_grpc.C2FServicer):

    def __init__(self, queue):
        self.queue = queue

    def C2F_getmsg(self, request, context):
        self.queue.put(request)
        return pb2.C2F_Response(flag=True)


class Setup(pb2_grpc.SetupServicer):

    def __init__(self, dic, server_port):
        self.dic = dic
        self.server_port = server_port

    def Setup_getmsg(self, request, context):
        self.dic[request.port] = request.batch
        self.server_port.append(request.port)
        print("Frontend target server config is {}".format(self.dic))
        # print(self.server_port)
        return pb2.S2C_Response(flag=True)


class Server:
    def __init__(self, port, aimport, height=224, width=224):
        """

        :param port: frontend port
        :param aimport:
        :param height:
        :param width:
        """
        self.server_port = []
        self.config = {}  # port-->batch对应关系
        self.port = port
        self.aim_port = aimport
        self.recv_q = Queue()
        self.target = 0
        self.send_q = Queue()
        self.width = width
        self.height = height
        self.schedule = Schedule(config=self.config,server_port=self.server_port,queue=self.send_q)

    def __server_run(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        pb2_grpc.add_C2FServicer_to_server(C2F(self.recv_q), server)
        pb2_grpc.add_SetupServicer_to_server(Setup(self.config, self.server_port), server)
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

    def __find_workload(self):

        target_port = self.server_port[self.target]
        print(self.target)
        self.target = (self.target + 1) % len(self.config)
        print("after {}".format(self.target))

        return target_port, self.config[target_port]



    def __send_service(self):
        print("q_data is detecting ---- ")
        count = 0
        while True:
            while not self.send_q.empty():  # 当队列不为空时
                port, batch = self.__find_workload()  # 获取server port
                count = count + 1
                print(port)
                req_list = []
                while batch:
                    if not self.send_q.empty():
                        batch = batch - 1
                        # print(batch)
                        req_list.append(self.send_q.get())

                self.__send_req(count, req_list)

    def __send_req(self, request_id, bytes_img):

        target_port = 'localhost:' + str(self.aim_port)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.F2SStub(channel)
            msg_send = pb2.F2S_Request(request_id=request_id, size=self.width, image=bytes_img)
            response = stub.F2S_getmsg(msg_send)

    def run(self):

        t1 = threading.Thread(target=self.__server_run)  # 启动服务端
        t2 = threading.Thread(target=self.__data_save)  # 启动转发端
        t3 = threading.Thread(target=self.__send_service)  # 启动发送端
        t1.start()
        t2.start()
        t3.start()


def main():
    s = Server(port=50001, aimport=50002)
    s.run()


if __name__ == '__main__':
    main()
