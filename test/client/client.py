#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 1:52 PM
# @Author  : Agonsle
# @Site    : 
# @File    : client.py.py
# @Software: PyCharm

"""
    schedule client
    1. zip image
    2. send image to frontend
"""
from concurrent import futures
import setproctitle
import time
import grpc
import numpy as np
import cv2  # BGR
from lib.mstime import delayMs as delayMs
import math
import threading
import lib.mstime as mytime
import conf.proto.test_proto.test_pb2 as pb2
import conf.proto.test_proto.test_pb2_grpc as pb2_grpc
from queue import Queue

_ONE_DAY_IN_SECONDS = 60 * 60
setproctitle.setproctitle("Client")

# class req_log:
#     def __init__(self):


class S2C(pb2_grpc.S2CServicer):
    def __init__(self, queue):
        self.q = queue

    def S2C_getmsg(self, request, context):
        for i in range(len(request.log)):
            request.log[i] = request.log[i] + " " + str(mytime.get_latency_ms(request.timestamp)) + " ms "
        # for log in request.log:
        print(request.log)
        self.q.put(request)
        # print(request.index)
        return pb2.S2C_Response(flag=True)


class Request:
    def __init__(self, send_time):
        self.send_time = send_time
        self.recv_time = None
        self.dur = None
        self.res = None


class Client:

    def __init__(self, path, port=50000, aimport=50001, SLOs=1000):
        self.path = path
        self.slos = SLOs
        self.latency = {}  # key:request id
        self.aim_port = aimport  # 靶机地址
        self.port = port  # 本机地址
        self.recv_q = Queue()  # 接收请求的队列

    def server_run(self):
        """
            启动Client接收端，默认端口是50000端口
        :return:
        """
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        pb2_grpc.add_S2CServicer_to_server(S2C(self.recv_q), server)
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

    def __image_parse(self):
        """
            预处理照片
        :return: bytes类型的图片，图片原始的长，宽
        """
        img_src = cv2.imread(self.path)
        img_src = cv2.resize(img_src, (224, 224), interpolation=cv2.INTER_AREA)
        h = img_src.shape[0]
        w = img_src.shape[1]
        img_byte = img_src.tobytes()
        return h, w, img_byte

    def __generate_Request(self):
        """
        随机生成请求类数据
        img = np.random.randint(0, 1, (224, 224, 3))
        img = img.astype("uint8")
        img = img.tobytes()
        """
        img = pb2.C2F_Request.Image()
        img.height, img.width, img.byte_image = self.__image_parse()
        return img

    def connect(self, msg_index, msg):
        """
        向frontend发送请求，frontend的端口为50001
        :param msg_index:
               img： sd
        :return:
        """
        target_port = 'localhost:' + str(self.aim_port)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.C2FStub(channel)
            log = "request_id "+ str(msg_index)+" "
            msg_send = pb2.C2F_Request(image=msg, request_id=msg_index, timestamp=mytime.get_timestamp(),log=log)

            r = Request(time.time())
            self.latency[msg_index] = r  # 保存每个请求的发送时间
            # st = time.time()
            stub.C2F_getmsg(msg_send)
            # print("send request time {:.3f} ms".format(1000 * (time.time() - st)))
            # print(response.flag)
            #12322

    def send_request(self):
        time.sleep(2)
        msg = self.__generate_Request()
        for i in range(10000):
            delayMs(20)
            # 生成测试数据
            print("send request {}".format(i + 1))
            self.connect(i + 1, msg)

    def __parse_result(self):
        print(" Client recieve part is loading")
        """
            Server -> Client msg
                - index：表明request_id
                - res：表明处理请求的id
        """
        while True:
            reqs = self.recv_q.get()
            count = 0
            for r in reqs.index:
                self.latency[r].recv_time = time.time()
                self.latency[r].res = reqs.res[count]
                self.latency[r].dur = self.latency[r].recv_time - self.latency[r].send_time
                print("request id {}, res is {},inference time is {:.3f}ms".format(r, self.latency[r].res,
                                                                                   1000 * self.latency[r].dur))
                count = count + 1

    def run(self):
        t1 = threading.Thread(target=self.send_request)
        # t2 = threading.Thread(target=self.server_run)
        # t3 = threading.Thread(target=self.__parse_result)
        t1.start()
        # t2.start()
        # t3.start()


def main():
    file_path = '../../img/test01.jpg'
    c = Client(port=50000, aimport=50001, path=file_path)
    c.run()


if __name__ == '__main__':
    main()
