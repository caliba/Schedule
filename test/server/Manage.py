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
        return pb2.S2D_Response(flag=True)


class Manage:
    """
    Manage:
        Step1: 根据输入的SLO 选择 throughoyt 最大的workload配置
        Step2: 启动Manage server 40000端口，暴露分别与workload和frontend连接的接口
                - 根据Step1中得出的workload的配置，初始化启动一台机器
        Step3: deamon通过检测Frontend处的throughput，来判断当前Manage下的workload能否满足这样的throughput的处理需求
                - 若worker的处理能力小于frontend的输入，则增设机器
                - 若worker处理能力大于frontend的输入，则停止机器（未实现）
    """

    def __init__(self, slo, port):
        self.port = port
        self.slo = slo
        self.frontend = Manage_F()  # 获取frontend的throughput
        self.max_throughput = 0  # 额定最大batchsize
        self.worker_thread = {}
        self.workerlist = {}
        self.profile = {1: 25, 2: 40}  # worker profile: batch->duration
        self.ip = 40003
        """ Step 1"""
        try:
            for key in self.profile:
                if self.profile[key] * 2 < self.slo:
                    self.max_throughput = int((0.85 * key * S_2_MS) / self.profile[key])  # 根据SLOs选择perferbatch
                else:
                    break
        except:
            print("error")

    def __server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        pb2_grpc.add_F2DServicer_to_server(F2D(self.frontend), server)
        pb2_grpc.add_S2DServicer_to_server(S2D(self.workerlist), server)
        port = '[::]:' + str(self.port)
        server.add_insecure_port(port)
        server.start()

        # Init single worker
        s = Server(port=40002, aimport=50000, feport=50001, model_name="VGG", profile=self.profile, slo=self.slo)
        self.workerlist[40002] = Manage_W(40002)
        self.worker_thread[40002] = s
        s.run()

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
                _prefer = math.ceil(self.frontend.throughput / self.max_throughput)  # 应该需要多少个workerload
                if _num < _prefer:
                    s = Server(port=self.ip, aimport=50000, feport=50001, model_name="VGG",
                               profile=self.profile, slo=self.slo)
                    self.workerlist[self.ip] = Manage_W(self.ip)
                    self.worker_thread[self.ip] = s
                    s.run()
                    self.ip = self.ip + 1
                elif _num > _prefer:  # 有空闲的机器
                    pass

    def run(self):
        t1 = threading.Thread(target=self.__daemon)
        t2 = threading.Thread(target=self.__server)
        t1.start()
        t2.start()


def main():
    Manage(slo=100, port=40000).run()


if __name__ == "__main__":
    main()
