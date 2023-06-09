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
import math
import threading
import lib.mstime as mytime
import conf.proto.test_proto.test_pb2 as pb2
import conf.proto.test_proto.test_pb2_grpc as pb2_grpc
from queue import Queue
import logging
import logging.config

_MS_TO_S = 0.001
_ONE_DAY_IN_SECONDS = 60 * 60
setproctitle.setproctitle("Client")
logging.config.fileConfig('../../log/logging.conf')
logger = logging.getLogger('client')

class S2C(pb2_grpc.S2CServicer):
    def __init__(self, queue):
        self.q = queue

    def S2C_getmsg(self, request, context):
        for i in range(len(request.servermessage)):
            request.servermessage[i].log = request.servermessage[i].log + " " + str(
                mytime.get_latency_ms(request.servermessage[i].timestamp[-1])) + " ms "
            request.servermessage[i].timestamp.append(mytime.get_timestamp())
            print(request.servermessage[i].log)
            # print(mytime.get_latency(request.servermessage[i].timestamp[0],request.servermessage[i].timestamp[-1]))
        self.q.put(request.servermessage)
        return pb2.S2C_Response(flag=True)


# request Client send to Frontend
class Request:
    def __init__(self, send_time):
        self.send_time = send_time
        self.recv_time = None
        self.dur = None
        self.res = None


class Client_config:
    def __init__(self, throughput=100):
        self.throughput = throughput
        self.send_req = 0
        self.reci_req = 0


class Client:

    def __init__(self, path, port=50000, aim_port=50001, SLOs=1000):
        self.path = path
        self.request_id = 1
        self.send_q = Queue()
        self.slos = SLOs
        self.config = Client_config()
        self.latency = {}  # key:request id
        self.aim_port = aim_port  # 靶机地址
        self.port = port  # 本机地址
        self.recv_q = Queue()  # 接收请求的队列
        self.stub = None

        target_port = 'localhost:' + str(self.aim_port)
        channel = grpc.insecure_channel(target_port)
        self.stub = pb2_grpc.C2FStub(channel)

    #

    def server_run(self):
        """
            启动Client接收端，默认端口是50000端口
        :return:
        """
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
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

    def __daemon(self):
        while True:
            history = self.config.send_req
            time.sleep(_MS_TO_S * 1000)
            now = self.config.send_req

    def connect(self):
        while True:
            req = self.send_q.get()
            log = "request_id " + str(self.request_id) + " "
            msg_send = pb2.C2F_Request(image=req, request_id=self.request_id, timestamp=mytime.get_timestamp(), log=log)
            r = Request(mytime.get_timestamp())
            self.latency[self.request_id] = r  # 保存每个请求的发送时间
            self.request_id = self.request_id + 1
            self.stub.C2F_getmsg(msg_send)

    def send_request(self):
        msg = self.__generate_Request()
        for i in range(10000):
            time.sleep(12.5 * _MS_TO_S)
            self.config.send_req = self.config.send_req + 1
            # 生成测试数据
            self.send_q.put(msg)

    def __parse_result(self):
        print(" Client recieve part is loading")
        while True:
            reqs = self.recv_q.get()
            # count = 0
            for r in reqs:
                idx = r.index
                self.latency[idx].recv_time = mytime.get_timestamp()
                self.latency[idx].dur = mytime.get_latency_ms(self.latency[idx].send_time)
                # print("request id {}, res is {},inference time is {:.3f}ms".format(idx, self.latency[idx].res,
                #                                                                    self.latency[idx].dur))
                # count = count + 1

    def run(self):

        t1 = threading.Thread(target=self.send_request)
        t2 = threading.Thread(target=self.server_run)
        t3 = threading.Thread(target=self.__parse_result)
        t4 = threading.Thread(target=self.__daemon)
        t5 = threading.Thread(target=self.connect)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()


def main():
    file_path = '../../img/test01.jpg'
    c = Client(port=50000, aim_port=50001, path=file_path)
    c.run()


if __name__ == '__main__':
    main()
