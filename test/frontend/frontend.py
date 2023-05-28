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
import logging.config
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

_MS_TO_S = 0.001
_ONE_DAY_IN_SECONDS = 60 * 60
setproctitle.setproctitle("Frontend")
logging.config.fileConfig('../../log/logging.conf')
frontend = logging.getLogger('frontend')


class F_Request:

    def __init__(self, data, request_id, log, arrive_time, send_time):
        self.data = data
        self.request_id = request_id
        self.log = log
        self.arrive_time = arrive_time  # 请求到达时间
        self.send_time = send_time  # 请求的发送时间


# Message Frontend
class FrontendMessage:
    def __init__(self, data, log, id, timestamp):
        self.data = data  # 存放数据data
        self.timestamp = timestamp  # 存放到达时间戳
        self.log = log  # 存放log
        self.id = id


class Worker:

    def __init__(self, port, batch, flag=True):
        self.batch = batch
        self.port = port
        self.data = []  # FrontendMessage
        self.stub = None
        self.flag = flag

        target_port = 'localhost:' + str(self.port)
        channel = grpc.insecure_channel(target_port)
        self.stub = pb2_grpc.F2SStub(channel)


class Frontend_config:
    """
    定义Frontend处的config,
    throughput : 吞吐量
    send_req: 发送请求个数
    """

    def __init__(self, throughput=0):
        self.throughput = throughput
        self.send_req = 0


class Request2S:
    def __init__(self, aim_port, data):
        self.aim_port = aim_port
        self.data = data


class C2F(pb2_grpc.C2FServicer):

    def __init__(self, queue, config):
        self.queue = queue
        self.config = config

    def C2F_getmsg(self, request, context):
        request.log = request.log + str(mytime.get_latency_ms(request.timestamp)) + str("ms ")
        r = F_Request(data=request.image, request_id=request.request_id, log=request.log,
                      arrive_time=mytime.get_timestamp(), send_time=request.timestamp)
        self.queue.put(r)
        self.config.send_req = self.config.send_req + 1  # 收到请求数量+1
        return pb2.C2F_Response(flag=True)


class Setup(pb2_grpc.SetupServicer):
    """
        register workload config in frontend
    """

    def __init__(self, worker, idx_dic, slo):
        self.idx_dic = idx_dic
        self.worker = worker
        self.slo = slo
        self.idx = 1

    def Setup_getmsg(self, request, context):
        self.idx_dic[self.idx] = request.port
        self.idx = self.idx + 1
        self.worker[request.port] = Worker(batch=request.batch,
                                           port=request.port)
        # print("Frontend Worker config : ")
        port_l = []
        batch = []
        for key in self.worker:
            port_l.append(self.worker[key].port)
            batch.append(self.worker[key].batch)
            # print("Worker Port {} prefer batch is {}".format(self.worker[key].port, self.worker[key].batch))
        frontend.info("Frontend Worker Config has been updated: Port list: {}, Batch list {}".format(port_l, batch))
        return pb2.Setup_Response(flag=True, slo=self.slo)


class Frontend:
    """
    Frontend：
        Step1：启动server:50001
                - 从client接受req
                - 从worker处接受配置信息，用于自身sheduler判断
        Step2: datasave:从client读取数据，放入recv_q
        Step3: preprocess req，从recv_q读取数据，进行数据预处理放入proc_q
        Step4: scheduler 根据RR或BA算法，向每个worker的queue中放入数据，满足要求后，放入send_q中
        Step5: 从send_q中读取数据，再向对应port的worker发送数据
        Step6: deamon：计算frontend的throughput，并发送给Manage
    """

    def __init__(self, port, size=224, policy="BA", barrier=5):
        self.worker = {}  # 与Frontend所连接的所有worker port->config的字典
        self.idx_dic = {}  # idx -> port 的字典
        self.slo = 100
        self.config = Frontend_config()
        self.request_id = 1  # server发送请求
        self.barrier = barrier  # SLOs
        self.policy = policy  # 使用何种分发策略
        self.port = port  # Frontend地址
        self.recv_q = Queue()  # 接收队列
        self.target = 1  # 哪台机器
        self.proc_q = Queue()  # 处理队列
        self.send_q = Queue()  # 发送队列
        self.size = size  # proc 图片大小
        self.MANAGE_FLAG = False

    def __server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        pb2_grpc.add_C2FServicer_to_server(C2F(self.recv_q, self.config), server)
        pb2_grpc.add_SetupServicer_to_server(
            Setup(
                worker=self.worker, idx_dic=self.idx_dic, slo=self.slo),
            server)
        port = '[::]:' + str(self.port)
        server.add_insecure_port(port)
        server.start()

        try:
            while True:
                frontend.info("Frontend Server is running")
                time.sleep(_ONE_DAY_IN_SECONDS)
                frontend.info("Frontend Server is over")
        except KeyboardInterrupt:
            server.stop(0)

    def __preprocess(self, req):
        request_id = req.request_id  # 请求序号
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
        p_req = pb2.F2S_Request.FrontendMessage()
        p_req.data = img
        p_req.id = request_id
        p_req.log = log
        p_req.timestamp.append(req.send_time)
        p_req.timestamp.append(req.arrive_time)

        return p_req

    def __data_save(self):
        frontend.info("Frontend Request Save Model is running")
        while True:
            req = self.recv_q.get()
            # self.config.send_req = self.config.send_req + 1
            self.proc_q.put(self.__preprocess(req))

    def __deamon(self):
        while True:
            history = self.config.send_req
            time.sleep(1000 * _MS_TO_S)
            now = self.config.send_req
            self.config.throughput = now - history
            # print("frontend throughput is {}".format(self.config.throughput))

    def __schedule(self):
        if self.policy == "RR":
            self.__RoundRobin()
        if self.policy == "BA":
            self.__BatchAware()

    def __add_send_q(self, worker):
        aim_port = worker.port
        data = copy.copy(worker.data)
        r = Request2S(aim_port=aim_port, data=data)
        self.send_q.put(r)

    def __RoundRobin(self):
        frontend.info("Scheduling policy RoundRobin")
        while True:
            req = self.proc_q.get()  # 获取分配的请求
            _worker = self.worker[self.idx_dic[self.target]]
            _worker.data.append(req)

            if len(_worker.data) == _worker.batch:
                self.__add_send_q(worker=_worker)
                # 发送完毕后再将发送队列清空
                self.Init_worker(_worker)
                self.request_id = self.request_id + 1

            # 寻找下一个worker
            self.target = self.target % len(self.worker) + 1

    def __BatchAware(self):
        frontend.info("Scheduling policy BatchAware")
        while True:
            while len(self.worker) == 0:
                pass
            _worker = self.worker[self.idx_dic[self.target]]
            _batch = _worker.batch
            batch = _batch

            while batch:
                req = self.proc_q.get()
                _worker.data.append(req)  # 包含id,log,timestamp,data
                batch = batch - 1
            self.__add_send_q(worker=copy.copy(_worker))

            # 发送完毕后再将发送队列清空

            self.request_id = self.request_id + 1
            # 寻找下一个worker
            self.target = self.target % len(self.worker) + 1
            self.Init_worker(_worker)

    def Init_worker(self, worker):
        worker.data.clear()

    def _Manage(self):
        # 当Frontend没有worker时
        while len(self.worker) == 0:
            pass
        target_port = 'localhost:' + str(40000)
        channel = grpc.insecure_channel(target_port)
        stub = pb2_grpc.F2DStub(channel)
        while True:
            time.sleep(1)
            msg_send = pb2.F2D_Request(throughput=int(self.config.throughput))  # 把当前throughput 发送给Manager
            stub.F2D_getmsg(msg_send)

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
            self.__send_req(req.aim_port, req.data)

    def __send_req(self, aim_port, data):
        stub = self.worker[aim_port].stub
        for i in range(len(data)):
            data[i].log = data[i].log + " " + str(
                mytime.get_latency_ms(data[i].timestamp[-1])) + " ms "
            data[i].timestamp.append(mytime.get_timestamp())
        msg_send = pb2.F2S_Request(request_id=1, size=self.size, frontendmessage=data)
        stub.F2S_getmsg(msg_send)

    def run(self):
        t1 = threading.Thread(target=self.__server, name="Server")  # 启动服务端
        t2 = threading.Thread(target=self.__data_save, name="Save")  # 启动转发端
        t3 = threading.Thread(target=self.__schedule, name="Scheduler")  # 启动发送端
        t4 = threading.Thread(target=self.send, name="Send")
        t5 = threading.Thread(target=self.__deamon, name="Deamon")
        t6 = threading.Thread(target=self._Manage, name="Manage")
        # t4 = threading.Thread(target=self.__Moniter)
        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()


def main():
    s = Frontend(port=50001, policy="BA")
    s.run()


if __name__ == '__main__':
    main()
