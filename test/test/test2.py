#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/10 10:31 PM
# @Author  : Agonsle
# @Site    : 
# @File    : test2.py
# @Software: PyCharm

import time
import numpy as np
import grpc
from concurrent import futures
import time
from tensorflow.keras.preprocessing.image import img_to_array
import threading
import conf.proto.msg_proto.msg_pb2 as pb2
import conf.proto.msg_proto.msg_pb2_grpc as pb2_grpc
import cv2


def send_req(img):
    target_port = 'localhost:' + str(50050)
    with grpc.insecure_channel(target_port) as channel:
        stub = pb2_grpc.TestStub(channel)
        msg_send = pb2.Test_Request(msg=1, img=img)
        send_time = time.time()
        response = stub.Test_getmsg(msg_send)
        print("frontend to server time is {:.3f}ms".format(1000 * (time.time() - send_time)))


def generate_data():
    img = np.random.randint(0, 1, (224, 224, 3))
    img = img.astype("uint8")
    return img.tobytes()


def bytes_to_numpy(image_bytes):
    image_np = np.frombuffer(image_bytes, dtype=np.uint8)
    image_np2 = cv2.imdecode(image_np, cv2.IMREAD_COLOR)
    return image_np2


def main():
    # img = np.random.randint(0, 1, (224,224,3))
    # img = img.astype("uint8")
    file_path = "../../img/test01.jpg"
    img_src = cv2.imread(file_path)
    img_src = cv2.resize(img_src, (224,224), interpolation=cv2.INTER_AREA)
    # print(type(img_src[0][0][1]))
    #
    # print(type(img[0][0][1]))
    img_src = img_src.tobytes()
    # print(len(img_src))
    # print(img.shape)
    # img = img.tobytes()
    # # img = bytes_to_numpy(img)
    # img = np.frombuffer(img, dtype=np.uint8)
    # img = img.reshape(224, 224, 3)
    # img = img_to_array(img)
    # print(type(img))
    # print(len(img))

    for i in range(10):
        send_req(img_src)


main()
