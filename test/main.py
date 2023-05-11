#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 10:33 PM
# @Author  : Agonsle
# @Site    : 
# @File    : main.py
# @Software: PyCharm
import time

# fp = "../img/test01.jpg"

from test.server.server import Server
from test.frontend.frontend import Frontend
from test.client.client import Client


def main():
    s = Frontend(port=50001, policy="BA")
    s.run()
    time.sleep(2)
    s1 = Server(port=50002, aimport=50000, feport=50001, model_name="VGG", batch=2)
    s1.run()
    time.sleep(2)
    file_path = '../img/test01.jpg'
    c = Client(port=50001, aimport=50000, path=file_path)
    c.run()

    pass


main()
