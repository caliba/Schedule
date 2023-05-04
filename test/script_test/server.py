#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/4/27 11:58 PM
# @Author  : Agonsle
# @Site    : 
# @File    : frontend.py
# @Software: PyCharm

from concurrent import futures
import grpc
import conf.proto.test_proto.test_pb2_grpc as test_pb2_grpc
import conf.proto.test_proto.test_pb2 as test_pb2
import time

_ONE_DAY_IN_SECONDS = 60 * 60
PORT = 50001
MAX_MESSAGE_LENGTH = 1024 * 1024 * 1024
options = [
    ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
    ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)
]

class Test(test_pb2_grpc.TestServicer):
    def Test_Getmsg(self, request, context):
        print(request.number)
        print(len(request.image))
        return test_pb2.Test_Response(response=True)


def myserver():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4),options=options)  # 设置最大连接数
    test_pb2_grpc.add_TestServicer_to_server(Test(), server)
    port = '[::]:' + str(PORT)
    server.add_insecure_port(port)  # 设置所有IP地址都可以访问, 端口号为50053 绑定端口号
    server.start()  # 启动服务

    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)  # 设置服务器启动一天, 一天后自动关闭
            print("时间到了, 该结束了")
    except KeyboardInterrupt:  # 如果出现ctr+c硬中断, 直接退出
        server.stop(0)


if __name__ == '__main__':
    myserver()