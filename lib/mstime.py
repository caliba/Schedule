#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 7:32 PM
# @Author  : Agonsle
# @Site    : 
# @File    : mstime.py
# @Software: PyCharm
import time
def delayMs(t):
    start, end = 0, 0
    start = time.time_ns()  # 精确至ns级别
    while (end - start < t * 1000000):
        end = time.time_ns()

