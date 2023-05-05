#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 11:54 AM
# @Author  : Agonsle
# @Site    : 
# @File    : Resnet50.py
# @Software: PyCharm
from tensorflow import keras
import time


class ResNet50:
    def __init__(self):
        self.model = self.__load_model()

    def __load_model(self):
        start_time = time.time()
        model = keras.applications.ResNet50(weights='imagenet', include_top=True)
        print(" Successful load model ResNet50 ! Load time: {:.3f}".format(time.time() - start_time))
        return model
