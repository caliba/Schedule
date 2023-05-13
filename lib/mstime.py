#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 7:32 PM
# @Author  : Agonsle
# @Site    : 
# @File    : mstime.py
# @Software: PyCharm
import time
import conf.proto.test_proto.test_pb2 as pb2
import conf.proto.test_proto.test_pb2_grpc as pb2_grpc


def delayMs(t):
    start, end = 0, 0
    start = time.time_ns()  # 精确至ns级别
    while (end - start < t * 1000000):
        end = time.time_ns()


def get_timestamp():
    _t = time.time()
    return pb2.Timestamp(
        seconds=int(_t),
        microseconds=int(_t * 1000000) % 1000000
    )


def get_latency_ms(timestamp):
    now = get_timestamp()
    sec = now.seconds - timestamp.seconds
    mics = now.microseconds - timestamp.microseconds
    return round(sec * 1000 + mics / 1000, 3)  # 保留三位小数
