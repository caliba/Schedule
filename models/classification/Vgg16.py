#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/3 10:04 AM
# @Author  : Agonsle
# @Site    : 
# @File    : Vgg16.py
# @Software: PyCharm
from tensorflow import keras
import time


class VGG16:
    def __init__(self):
        self.model = self.__load_model()

    def __load_model(self):
        start_time = time.time()
        model = keras.applications.VGG16(weights='imagenet', include_top=True)
        print(" Successful load model VGG16 ! Load time: {:.3f}".format(time.time() - start_time))
        return model



