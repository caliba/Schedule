#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/4/27 10:20 AM
# @Author  : Agonsle
# @Site    : 
# @File    : imgtobytes.py
# @Software: PyCharm

import base64
import sys
import time
import grpc
import numpy as np
import cv2  # BGR
import math
import conf.proto.test_proto.test_pb2_grpc as test_pb2_grpc
import conf.proto.test_proto.test_pb2 as test_pb2
import lib.Class_image as CImage

PIC_WEITH = 224
PIC_HEIGHT = 224


def run(msg, bytes_data):  # 定义一个频道
    with grpc.insecure_channel('localhost:50001') as channel:  # 定义一个频道
        stub = test_pb2_grpc.TestStub(channel)  ## 指定channel 生成client
        t = test_pb2.Test_Request.Image()
        t.height = 853
        t.width = 1280
        t.img = bytes_data
        msg_send = test_pb2.Test_Request(image=[t,t], number=[1,2])
        response = stub.Test_Getmsg(msg_send)
        print(response.response)


def img_preprocess(file_path):
    img = cv2.imread(file_path)
    # print(type(img))
    # print(img.dtype) # 数据类型
    print(img.shape[0]) # 形状
    # h,w = img.shape
    # print(h)
    # print(w)
    # print(img.size) # 大小

    img = cv2.resize(img, (PIC_WEITH, PIC_HEIGHT), interpolation=cv2.INTER_AREA)
    img = np.array(img)
    img = (img / 127.5) - 1
    # print(img.shape)
    # print(img.dtype)
    cv2.imshow("sdd", img)
    cv2.waitKey(0)

    # pass


# 图片img转化为bytes类型
def img2bytes(file_path):
    img_src = cv2.imread(file_path)
    img_byte = img_src.tobytes()
    return img_byte


# bytes再转化为可处理的img
def bytes2img(img_bytes):
    nparr = np.frombuffer(img_bytes, dtype=np.uint8)
    nparr = nparr.reshape(853, 1280,3)
    img = cv2.resize(nparr, (PIC_WEITH, PIC_HEIGHT), interpolation=cv2.INTER_AREA)
    # cv2.imshow("sdsd",img)
    # cv2.waitKey()
    img = img.tobytes()
    # print(img)

def main():
    file_path = '../../img/test01.jpg'
    img_bytes = img2bytes(file_path)
    h = 853
    w = 1280
    bytes2img(img_bytes)
    # img_preprocess(file_path)

    # c = CImage.Image(h,w,img_bytes)
    # print(c)
    #
    # start_time = time.time()
    for i in range(3):
        print("发送了第{}个请求,发送时间是{}".format(i + 1, time.time()))

        time.sleep(1)
        run(i + 1, img_bytes)
    # print("send request totally cost {:.3f}".format(time.time() - start_time))


if __name__ == '__main__':
    main()
