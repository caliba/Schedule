#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 1:52 PM
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
import setproctitle
import numpy as np
import cv2  # BGR
import copy
import math
import conf.proto.test_proto.test_pb2 as pb2
import conf.proto.test_proto.test_pb2_grpc as pb2_grpc
from queue import Queue
import lib.mstime as mytime

_ONE_DAY_IN_SECONDS = 60 * 60
setproctitle.setproctitle("Frontend")


class F_Request:

    def __init__(self, img, request_id, log):
        self.img = img
        self.request_id = request_id
        self.log = log


class Worker:

    def __init__(self, port, batch):
        self.id = []
        self.batch = batch
        self.port = port
        self.data = []
        self.log = []
        self.stub = None

        target_port = 'localhost:' + str(self.port)
        channel = grpc.insecure_channel(target_port)
        self.stub = pb2_grpc.F2SStub(channel)


class Request2S:
    def __init__(self, aim_port, request_id, bytes_img, index, log):
        self.aim_port = aim_port
        self.request_id = request_id
        self.bytes_img = bytes_img
        self.index = index
        self.log = log


class C2F(pb2_grpc.C2FServicer):
    """
        grpc client to frontend
    """

    def __init__(self, queue, arrive_time, grpc_time):
        self.queue = queue
        self.grpc_time = grpc_time
        self.arrive_time = arrive_time

    def C2F_getmsg(self, request, context):
        request.log = request.log + str(mytime.get_latency_ms(request.timestamp)) + str("ms ")
        print(request.log)
        self.queue.put(request)
        self.arrive_time.append(mytime.get_timestamp())  # 请求到达时间存放
        # print(request.log)
        # print(mytime.get_latency_ms(request.timestamp))
        # print(request.request_id)
        # print("send time {}".format(request.send_time))
        # print("time is {}".format(time.time()))
        # print("client to server grpc time is {:.3f}".format(time.time()-request.send_time))
        return pb2.C2F_Response(flag=True)


class Setup(pb2_grpc.SetupServicer):
    """
        register workload config in frontend
    """

    def __init__(self, dic, server_port, list_q, id_q, q_start, log_q, stub, worker):
        self.dic = dic
        self.worker = worker
        self.stub = stub
        self.q_start = q_start
        self.log_q = log_q
        self.list_q = list_q
        self.id_q = id_q
        self.server_port = server_port

    def Setup_getmsg(self, request, context):
        # self.worker.append(Worker(batch=request.batch,
        #                                    port=request.port))
        self.dic[request.port] = request.batch
        self.server_port.append(request.port)
        target_port = 'localhost:' + str(request.port)
        channel = grpc.insecure_channel(target_port)
        # with grpc.insecure_channel(target_port) as channel:
        stub = pb2_grpc.F2SStub(channel)
        self.stub.append(stub)
        self.list_q.append([])
        self.log_q.append([])
        self.q_start.append(0)
        self.id_q.append([])
        print("Frontend target server config is {}".format(self.dic))
        # print(self.server_port)
        return pb2.S2C_Response(flag=True)


class Frontend:
    def __init__(self, port, height=224, width=224, policy="BA", barrier=5):
        """

        :param port: Frontend ip
        :param height: preprocess img height
        :param width: preprocess img width
        """
        self.worker = []
        self.stub = []
        self.log_q = []  # 用于存放log
        self.grpc_time = []
        self.barrier = barrier
        self.arrive_time = []  # 用与存放每个请求到达的时间
        self.policy = policy
        self.server_port = []
        self.config = {}  # port-->batch对应关系
        self.port = port
        self.list_q = []  # 每组数据的图片
        self.id_q = []  # 每组数据的id
        self.q_start = []
        self.recv_q = Queue()
        self.target = 0
        self.send_q = Queue()
        self.send_QQ = Queue()
        self.width = width
        self.height = height

    def __server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        pb2_grpc.add_C2FServicer_to_server(C2F(self.recv_q, self.arrive_time, self.log_q), server)
        pb2_grpc.add_SetupServicer_to_server(
            Setup(self.config, self.server_port, self.list_q, self.id_q, self.q_start, self.log_q, self.stub,
                  self.worker),
            server)
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
        request_id = req.request_id  # 请求序号
        log = req.log  # 请求log
        h = req.image.height
        w = req.image.width
        img_bytes = req.image.byte_image
        # pic resize
        img = np.frombuffer(img_bytes, dtype=np.uint8)
        img = img.reshape(h, w, 3)
        img = cv2.resize(img, (self.width, self.height), interpolation=cv2.INTER_AREA)
        # pic to bytes
        img = img.tobytes()
        # 处理一张图片，其返回值是一个类，包含图片信息和请求id
        return F_Request(img=img, request_id=request_id, log=log)

    def __data_save(self):
        print("data save is running -- ")
        while True:
            mytime.delayMs(1)
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
                req = self.send_q.get()  # 获取分配的请求
                # # add
                # _worker = self.worker[index]

                # 将 id img存入对应的id
                self.id_q[index].append(req.request_id)
                self.list_q[index].append(req.img)
                self.log_q[index].append(req.log)
                print(" index {} len {}".format(index, len(self.list_q[index])))
                if len(self.list_q[index]) == self.config[self.server_port[index]]:
                    aim_port = self.server_port[index]
                    bytes_img = self.list_q[index]
                    t1 = threading.Thread(target=self.__send_req,
                                          kwargs={'aim_port': self.server_port[index], 'request_id': request_id,
                                                  'bytes_img': bytes_img, 'index': self.id_q[index]})
                    t1.start()
                    t1.join()
                    self.list_q[index].clear()
                    self.id_q[index].clear()
                    request_id = request_id + 1
                index = (index + 1) % len(self.config)

    def __BatchAware(self):
        print("--- Scheduling policy BatchAware ---")
        index = 0
        request_id = 1
        while True:
            while len(self.server_port) == 0:
                pass
            port = self.server_port[index]  # 获取worker的port
            batch = self.config[port]  # 获取 prefer batch
            # add
            # _worker = self.worker[index]
            # _batch = _worker.batch


            while batch:
                req = self.send_q.get()  # 从队列中取出一个请求
                # # add
                # _worker.data.append(req.img)
                # _worker.log.append(req.log)
                # _worker.id.append(req.request_id)


                self.id_q[index].append(req.request_id)
                self.log_q[index].append(req.log)
                self.list_q[index].append(req.img)
                if len(self.list_q[index]) == 1:  # 如果这个请求是第一个请求
                    self.q_start[index] = time.time()

                batch = batch - 1

            for i in range(len(self.log_q[index])):
                idx = self.id_q[index][i]  # 获取请求id
                arrive_t = self.arrive_time[idx - 1]  #
                res = mytime.get_latency_ms(arrive_t)
                self.log_q[index][i] = str(self.log_q[index][i]) + " " + str(res) + "ms "
            # print(id(self.id_q[index]))
            # add
            # print("sb")
            # print(_worker.log)
            # for log in _worker.log:
            #     pass

            aim_port = copy.copy(self.server_port[index])
            bytes_img = copy.copy(self.list_q[index])
            _index = copy.copy(self.id_q[index])
            print(id(_index))
            log = copy.copy(self.log_q[index])
            r = Request2S(aim_port=aim_port, request_id=request_id, bytes_img=bytes_img,
                          index=_index, log=log)
            self.send_QQ.put(r)

            # 发送完毕后再将发送队列清空
            self.list_q[index].clear()
            self.id_q[index].clear()
            self.log_q[index].clear()
            self.q_start[index] = 0
            # 寻找下一个worker
            index = (index + 1) % len(self.config)

    def __Moniter(self):
        print("Frontend guard moniter is running ")
        while True:
            while len(self.list_q) != 0:  # 有server被加入
                for index in range(len(self.list_q)):
                    start_time = self.q_start[index]  # 获取这个队列的启动时间
                    if start_time != 0:  # 当这个队列中有请求时
                        dur = time.time() - start_time  # 计算队列收集到了多久
                        if dur > self.barrier:  # 如果队列等待时间大于5s
                            print("提前send,{}".format(self.id_q[index]))
                            t1 = threading.Thread(target=self.__send_req,
                                                  kwargs={'aim_port': self.server_port[index], 'request_id': 1,
                                                          'bytes_img': self.list_q[index], 'index': self.id_q[index],
                                                          'log': self.log_q[index]})
                            t1.start()
                            t1.join()
                            self.list_q[index].clear()
                            self.id_q[index].clear()
                            self.q_start[index] = 0

        pass

    def __guard(self):
        pass

    def send(self):
        while True:
            req = self.send_QQ.get()
            print(req.log)
            print(req.index)
            self.__send_req(req.aim_port, req.request_id, req.bytes_img, req.index, req.log)

    def __send_req(self, aim_port, request_id, bytes_img, index, log):
        # target_port = 'localhost:' + str(aim_port)
        # print("send")
        # print(log)
        # with grpc.insecure_channel(target_port) as channel:
        #     stub = pb2_grpc.F2SStub(channel)
        stub = self.stub[0]
        msg_send = pb2.F2S_Request(request_id=request_id, size=self.width, image=bytes_img, index=index,
                                   timestamp=mytime.get_timestamp(), log=log)
        send_time = time.time()
        response = stub.F2S_getmsg(msg_send)
        print(response)
        print("frontend to server time is {:.3f}".format(1000 * (time.time() - send_time)))

    def run(self):

        t1 = threading.Thread(target=self.__server)  # 启动服务端
        t2 = threading.Thread(target=self.__data_save)  # 启动转发端
        t3 = threading.Thread(target=self.__schedule)  # 启动发送端
        t4 = threading.Thread(target=self.send)
        # t4 = threading.Thread(target=self.__Moniter)
        t1.start()
        t2.start()
        t3.start()
        t4.start()


def main():
    s = Frontend(port=50001, policy="BA")
    s.run()


if __name__ == '__main__':
    main()
