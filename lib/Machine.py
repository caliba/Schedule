#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 11:01 AM
# @Author  : Agonsle
# @Site    : 
# @File    : Machine.py
# @Software: PyCharm
from queue import Queue
import conf.proto.msg_proto.msg_pb2 as pb2
import conf.proto.msg_proto.msg_pb2_grpc as pb2_grpc
import grpc

class Machine:

    def __init__(self, port, aimport):
        self.port = port
        self.aim_port = aimport
        self.recv_q = Queue()  # reqs from client
        self.send_q = Queue()  # reqs send to server

    def __send_req(self):
        target_port = 'localhost:' + str(self.aim_port)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.F2SStub(channel)
            msg_send = pb2.F2S_Request()
            response = stub.F2S_getmsg(msg_send)
