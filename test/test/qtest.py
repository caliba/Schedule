#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/11 4:26 PM
# @Author  : Agonsle
# @Site    : 
# @File    : qtest.py
# @Software: PyCharm
import copy
from queue import Queue
class tx:

    def __init__(self):
        self.a = []
        self.b = []

a = ["sds","sds1","ssaq"]
b = [1,2,3]
print(id(a[0]))
# for c in a:
#     print(id(c))
#     c = c+"sb"
#     print(id(c))
#     print("---")

# print(a)

for i in b:
    i = copy.copy(i+1)

print(b)