#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/4/29 9:40 AM
# @Author  : Agonsle
# @Site    : 
# @File    : server.py
# @Software: PyCharm
import random
import threading
import time
import grpc
from concurrent import futures
import numpy as np
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
from models.classification import Classification as Models
import conf.proto.msg_proto.msg_pb2 as pb2
import conf.proto.msg_proto.msg_pb2_grpc as pb2_grpc
from queue import Queue

_ONE_DAY_IN_SECONDS = 60 * 60


class F2S(pb2_grpc.F2SServicer):

    def __init__(self, queue):
        self.queue = queue

    def F2S_getmsg(self, request, context):
        self.queue.put(request)
        # print(request.index)
        return pb2.F2S_Response(flag=True)


class Server:
    def __init__(self, port, aimport, feport, model_name, batch=1):
        """

        :param port: server port
        :param aimport: client port
        :param feport:  frontend port
        :param batch:   server process batch
        """
        self.model_name = model_name
        self.port = port
        self.model = None
        self.batch = batch
        self.feport = feport
        self.aim_port = aimport
        self.queue = Queue()

        # send server config to frontend
        target_port = 'localhost:' + str(self.feport)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.SetupStub(channel)
            msg_send = pb2.Setup_Request(port=str(self.port), batch=self.batch)
            res = stub.Setup_getmsg(msg_send)

    def __load_model(self):
        if self.model_name == "VGG":
            return Models.VGG16().model
        elif self.model_name == "ResNet50":
            return Models.ResNet50().model

    def __data_parse(self, bytes_img, size):
        img = np.frombuffer(bytes_img, dtype=np.uint8)
        img = img.reshape(size, size, 3)
        return img

    def __parse_batch(self, reqs, size):
        batch = []
        for req in reqs:
            img = np.frombuffer(req, dtype=np.uint8)
            img = img.reshape(size, size, 3)
            img = img_to_array(img)
            batch.append(img)

        return tf.convert_to_tensor(batch, dtype=tf.float32)

    def __model(self):
        # loading model
        self.model = self.__load_model()

        while True:
            while not self.queue.empty():
                # prepare image data
                reqs = self.queue.get()
                size = reqs.size
                request_id = reqs.index
                res_list = []
                batch = self.__parse_batch(reqs.image, size)
                # model inference
                start_time = time.time()
                res = self.model.predict(batch)
                latency = time.time() - start_time
                res = keras.applications.vgg16.decode_predictions(res)
                for r in res:
                    res_list.append(r[0][1])
                print("Port {}: message lens {} spend time {:.3f} s".format(self.port, len(res), latency))

                self.__send_data(res_list, request_id=request_id)

    def __server(self):
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
        pb2_grpc.add_F2SServicer_to_server(F2S(self.queue), server)
        port = '[::]:' + str(self.port)
        server.add_insecure_port(port)
        server.start()

        try:
            while True:
                print("server is running")
                time.sleep(_ONE_DAY_IN_SECONDS)
                print("server is over")
        except KeyboardInterrupt:
            server.stop(0)

    def __send_data(self, res, request_id):
        target_port = 'localhost:' + str(self.aim_port)
        with grpc.insecure_channel(target_port) as channel:
            stub = pb2_grpc.S2CStub(channel)
            msg_send = pb2.S2C_Request(res=res, index=request_id)
            stub.S2C_getmsg(msg_send)

    def run(self):
        t1 = threading.Thread(target=self.__server)
        t2 = threading.Thread(target=self.__model)
        t1.start()
        t2.start()


def main():
    s = Server(port=50002, aimport=50000, feport=50001, model_name="VGG", batch=2)
    s2 = Server(port=50003, aimport=50000, feport=50001, model_name="VGG", batch=2)
    s2.run()
    s.run()


if __name__ == '__main__':
    main()
