#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 11:52 AM
# @Author  : Agonsle
# @Site    : 
# @File    : connect_to_client.py
# @Software: PyCharm

import random
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

_ONE_DAY_IN_SECONDS = 60 * 60


def test_S2C():
    target_port = 'localhost:' + str(50003)
    for i in range(5):
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.S2CStub(channel)
            msg_send = pb2.S2C_Request(res = ['class1','class1'])
            res = stub.S2C_getmsg(msg_send)
            print(res)
def test_S2F():
    target_port = 'localhost:' + str(50001)
    for i in range(3):
        print("send")
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.SetupStub(channel)
            msg_send = pb2.Setup_Request(port = "50001",batch = 2)
            res = stub.Setup_getmsg(msg_send)
            print(res)

def main():
    test_S2F()

if __name__ =='__main__':
    main()