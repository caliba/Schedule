#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/4/28 11:03 AM
# @Author  : Agonsle
# @Site    : 
# @File    : client.py
# @Software: PyCharm

"""
    schedule client
    1. zip image
    2. send image to frontend
"""
from concurrent import futures
import time
import grpc
import numpy as np
import cv2  # BGR
import math
import threading
import conf.proto.msg_proto.msg_pb2 as pb2
import conf.proto.msg_proto.msg_pb2_grpc as pb2_grpc
from queue import Queue

_ONE_DAY_IN_SECONDS = 60 * 60


class S2C(pb2_grpc.S2CServicer):
    def __init__(self, queue):
        self.q = queue

    def S2C_getmsg(self, request, context):
        self.q.put(request.res)
        print(request.res)
        print(len(request.res))
        return pb2.S2C_Response(flag=True)


class Client:

    def __init__(self, port, aimport, path):
        self.path = path
        self.aim_port = aimport
        self.port = port
        self.recv_q = Queue()

    def server_run(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        pb2_grpc.add_S2CServicer_to_server(S2C(self.recv_q), server)
        port = '[::]:' + str(self.aim_port)
        server.add_insecure_port(port)
        server.start()

        try:
            while True:
                print("server is running")
                time.sleep(_ONE_DAY_IN_SECONDS)  # 设置服务器启动一天, 一天后自动关闭
                print("server is over")
        except KeyboardInterrupt:  # 如果出现ctr+c硬中断, 直接退出
            server.stop(0)

    def __image_parse(self):
        img_src = cv2.imread(self.path)
        h = img_src.shape[0]
        w = img_src.shape[1]
        img_byte = img_src.tobytes()
        return h, w, img_byte

    def __generate_Request(self):
        img = pb2.C2F_Request.Image()
        img.height, img.width, img.byte_image = self.__image_parse()
        return img

    def connect(self, msg_index):
        target_port = 'localhost:' + str(self.port)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.C2FStub(channel)
            img = self.__generate_Request()
            msg_send = pb2.C2F_Request(image=img, request_id=msg_index)
            response = stub.C2F_getmsg(msg_send)
            # print(response.flag)

    def send_request(self):
        for i in range(7):
            time.sleep(2)
            print("send request {}".format(i + 1))
            self.connect(i + 1)

    def run(self):
        t1 = threading.Thread(target=self.send_request)
        t2 = threading.Thread(target=self.server_run)
        t1.start()
        t2.start()


def main():
    file_path = '../../img/test01.jpg'
    c = Client(port=50001, aimport=50000, path=file_path)
    c.run()


if __name__ == '__main__':
    main()
