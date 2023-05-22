#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/20 6:03 PM
# @Author  : Agonsle
# @Site    : 
# @File    : Manage.py
# @Software: PyCharm
import threading

import grpc
import math
import conf.proto.test_proto.test_pb2 as pb2
import conf.proto.test_proto.test_pb2_grpc as pb2_grpc
from queue import Queue
from concurrent import futures
from server import Server
import time

S_2_MS = 1000
_ONE_DAY_IN_SECONDS = 60 * 60


class Manage_F:
    def __init__(self):
        self.throughput = 0


class Manage_W:
    def __init__(self, port):
        self.throughput = 0
        self.port = port
        self.flag = True  # 是否正在运转


class F2D(pb2_grpc.F2DServicer):

    def __init__(self, frontend):
        self.frontend = frontend

    def F2D_getmsg(self, request, context):
        self.frontend.throughput = request.throughput
        return pb2.F2D_Response(flag=True)


class S2D(pb2_grpc.S2DServicer):

    def __init__(self, worklist):
        self.worklist = worklist

    def S2D_getmsg(self, request, context):
        # port throughput max_throughput
        self.worklist[int(request.port)].throughput = request.throughput  # 更新worker的throughput

        print("122131231 {}".format(request.throughput))
        return pb2.S2D_Response(flag=True)


class Manage:

    def __init__(self, slo):
        self.port = 40000
        self.slo = slo
        self.frontend = Manage_F()  # 获取frontend的throughput
        self.max_throughput = 0  # 额定最大batchsize
        self.worker_thread = {}
        self.workerlist = {}
        self.profile = {1: 25, 2: 40}  # worker profile batch->duration
        self.ip = 50003

        try:
            for key in self.profile:
                if self.profile[key] * 2 < self.slo:
                    self.max_throughput = int((0.85 * key * S_2_MS) / self.profile[key])  # 根据SLOs选择perferbatch
                else:
                    break
        except:
            print("error")

        # Init worker
        s = Server(port=50002, aimport=50000, feport=50001, model_name="VGG", profile=self.profile, slo=self.slo)
        self.workerlist[50002] = Manage_W(50002)
        self.worker_thread[50002] = s
        s.run()
        # self.worker_thread.append(s)

    def __server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        pb2_grpc.add_F2DServicer_to_server(F2D(self.frontend), server)
        pb2_grpc.add_S2DServicer_to_server(S2D(self.workerlist), server)
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

    def __daemon(self):
        while True:
            time.sleep(1)
            print("frontend throughput is {}".format(self.frontend.throughput))
            if self.frontend.throughput != 0:
                _num = len(self.workerlist)  # 现在有多少个workload
                _prefer = math.ceil(self.frontend.throughput / self.max_throughput) # 应该需要多少个workerload
                if _num < _prefer:
                # if self.frontend.throughput > _num * self.max_throughput:  # 如果小于throughput 那么就开一个
                    s = Server(port=self.ip, aimport=50000, feport=50001, model_name="VGG",
                               profile=self.profile, slo=self.slo)
                    self.workerlist[self.ip] = Manage_W(self.ip)
                    self.worker_thread[self.ip] = s
                    s.run()
                    self.ip = self.ip + 1
                elif _num > _prefer: # 有空闲的机器
                    pass



    def run(self):
        t1 = threading.Thread(target=self.__daemon)
        t2 = threading.Thread(target=self.__server)
        t1.start()
        t2.start()


def main():
    Manage(slo=100).run()


if __name__ == "__main__":
    main()
