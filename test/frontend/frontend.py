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
import cv2
import copy
import conf.proto.test_proto.test_pb2_grpc as pb2_grpc
import conf.proto.test_proto.test_pb2 as pb2

from queue import Queue
import lib.mstime as mytime

_ONE_DAY_IN_SECONDS = 60 * 60
setproctitle.setproctitle("Frontend")


class F_Request:

    def __init__(self, data, request_id, log, arrive_time, send_time):
        self.data = data
        self.request_id = request_id
        self.log = log
        self.timestamp = []
        self.arrive_time = arrive_time  # 请求到达时间
        self.send_time = send_time  # 请求的发送时间


class Worker:

    def __init__(self, port, batch):
        self.id = []
        self.batch = batch
        self.port = port
        self.arrive_time = []
        self.send_time = []
        self.data = []
        self.log = []
        self.stub = None

        target_port = 'localhost:' + str(self.port)
        channel = grpc.insecure_channel(target_port)
        self.stub = pb2_grpc.F2SStub(channel)


class Request2S:
    def __init__(self, aim_port, request_id, bytes_img, index, log, send_time):
        self.aim_port = aim_port
        self.request_id = request_id
        self.bytes_img = bytes_img
        self.index = index
        self.log = log
        self.send_time = send_time


class C2F(pb2_grpc.C2FServicer):
    """
        grpc client to frontend
    """

    def __init__(self, queue):
        self.queue = queue

    def C2F_getmsg(self, request, context):
        request.log = request.log + str(mytime.get_latency_ms(request.timestamp)) + str("ms ")
        r = F_Request(data=request.image, request_id=request.request_id, log=request.log,
                      arrive_time=mytime.get_timestamp(), send_time=request.timestamp)
        self.queue.put(r)
        return pb2.C2F_Response(flag=True)


class Setup(pb2_grpc.SetupServicer):
    """
        register workload config in frontend
    """

    def __init__(self, worker, idx_dic):
        self.idx_dic = idx_dic
        self.worker = worker
        self.idx = 1

    def Setup_getmsg(self, request, context):
        self.idx_dic[self.idx] = request.port
        self.idx = self.idx + 1
        self.worker[request.port] = Worker(batch=request.batch,
                                           port=request.port)
        for key in self.worker:
            print("Worker Port: {} Batch: {} ".format(self.worker[key].port, self.worker[key].batch))

        return pb2.S2C_Response(flag=True)


class Frontend:
    def __init__(self, port, size=224, policy="BA", barrier=5):
        """

        :param port:
        :param size:
        :param policy:
        :param barrier:
        """
        self.worker = {}  # 与Frontend所连接的所有worker port->config的字典
        self.idx_dic = {}  # idx -> port 的字典
        self.request_id = 1  # server发送请求
        self.barrier = barrier  # SLOs
        self.policy = policy  # 使用何种分发策略
        self.port = port  # Frontend地址
        self.recv_q = Queue()  # 接收队列
        self.target = 1  # 哪台机器
        self.proc_q = Queue()  # 处理队列
        self.send_q = Queue()  # 发送队列
        self.size = size  # proc 图片大小

    def __server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        pb2_grpc.add_C2FServicer_to_server(C2F(self.recv_q), server)
        pb2_grpc.add_SetupServicer_to_server(
            Setup(
                worker=self.worker, idx_dic=self.idx_dic),
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
        timestamp = req.arrive_time
        log = req.log  # 请求log
        h = req.data.height
        w = req.data.width
        img_bytes = req.data.byte_image
        # pic resize
        img = np.frombuffer(img_bytes, dtype=np.uint8)
        img = img.reshape(h, w, 3)
        img = cv2.resize(img, (self.size, self.size), interpolation=cv2.INTER_AREA)
        # pic to bytes
        img = img.tobytes()
        # 处理一张图片，其返回值是一个类，包含图片信息和请求id
        return F_Request(data=img, request_id=request_id, log=log, arrive_time=timestamp, send_time=req.send_time)

    def __data_save(self):
        print("data save is running -- ")
        while True:
            mytime.delayMs(1)
            req = self.recv_q.get()
            self.proc_q.put(self.__preprocess(req))

    def __schedule(self):
        if self.policy == "RR":
            self.__RoundRobin()
        if self.policy == "BA":
            self.__BatchAware()

    def __add_send_q(self, worker):
        aim_port = worker.port
        send_time = copy.copy(worker.send_time)
        bytes_img = copy.copy(worker.data)
        _index = copy.copy(worker.id)
        log = copy.copy(worker.log)
        r = Request2S(aim_port=aim_port, request_id=self.request_id, bytes_img=bytes_img,
                      index=_index, log=log, send_time=send_time)
        self.send_q.put(r)

    def __RoundRobin(self):
        print("--- Scheduling policy RoundRobin ---")
        while True:
            req = self.proc_q.get()  # 获取分配的请求
            _worker = self.worker[self.idx_dic[self.target]]
            # 将 id img存入对应的id
            _worker.data.append(req.data)
            _worker.send_time.append(req.send_time)
            _worker.arrive_time.append(req.arrive_time)
            _worker.log.append(req.log)
            _worker.id.append(req.request_id)
            if len(_worker.id) == _worker.batch:
                for i in range(_worker.batch):
                    _worker.log[i] = _worker.log[i] + " " + str(
                        mytime.get_latency_ms(_worker.arrive_time[i])) + " ms "

                self.__add_send_q(worker=_worker)
                # 发送完毕后再将发送队列清空
                self.Init_worker(_worker)
                self.request_id = self.request_id + 1

            # 寻找下一个worker
            self.target = self.target % len(self.worker) + 1

    def __BatchAware(self):
        print("--- Scheduling policy BatchAware ---")
        while True:
            while len(self.worker) == 0:
                pass

            _worker = self.worker[self.idx_dic[self.target]]
            _batch = _worker.batch
            batch = _batch

            while batch:
                req = self.proc_q.get()
                _worker.data.append(req.data)
                _worker.arrive_time.append(req.arrive_time)
                _worker.send_time.append(req.send_time)
                # req.log = req.log + " " + str(mytime.get_latency_ms(req.arrive_time)) + " ms "
                _worker.log.append(req.log)
                _worker.id.append(req.request_id)
                batch = batch - 1

            for i in range(_batch):
                _worker.log[i] = _worker.log[i] + " " + str(mytime.get_latency_ms(_worker.arrive_time[i])) + " ms "

            self.__add_send_q(worker=_worker)

            # 发送完毕后再将发送队列清空
            self.Init_worker(_worker)
            self.request_id = self.request_id + 1

            # 寻找下一个worker
            self.target = self.target % len(self.worker) + 1

    def Init_worker(self, worker):
        worker.log.clear()
        worker.id.clear()
        worker.arrive_time.clear()
        worker.data.clear()

    """
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
    """

    def __guard(self):
        pass

    def send(self):
        while True:
            req = self.send_q.get()
            self.__send_req(req.aim_port, req.request_id, req.bytes_img, req.index, req.log, req.send_time)

    def __send_req(self, aim_port, request_id, bytes_img, index, log, send_time):
        stub = self.worker[aim_port].stub
        msg_send = pb2.F2S_Request(request_id=request_id, size=self.size, image=bytes_img, index=index,
                                   timestamp=mytime.get_timestamp(), log=log, send_time=send_time)
        stub.F2S_getmsg(msg_send)

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
