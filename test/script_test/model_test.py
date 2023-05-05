#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/5 11:30 AM
# @Author  : Agonsle
# @Site    : 
# @File    : model_test.py
# @Software: PyCharm

from models.classification import Classification as Model
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.image import load_img
import time


def load_model():
    model = Model.VGG16().model
    return model


def parse_pic():
    img_path = '../../img/test01.jpg'
    image = load_img(img_path, target_size=(224, 224))
    image = img_to_array(image)

    image = img_to_array(image)
    image = tf.convert_to_tensor(image, dtype=tf.float32)
    image = image[tf.newaxis, ...]
    # image = tf.expand_dims(image, 0)
    return image


def parse_batch():
    img_path = '../../img/test01.jpg'
    batch = []
    count = 0
    while count < 2:
        image = load_img(img_path, target_size=(224, 224))
        image = img_to_array(image)
        batch.append(image)
        count = count + 1

    return tf.convert_to_tensor(batch, dtype=tf.float32)


def main():
    # img = parse_pic()
    img = parse_batch()
    model = load_model()
    print(img.shape)
    for i in range(3):
        start_time = time.time()
        res = model.predict(img)
        res = keras.applications.vgg16.decode_predictions(res)
        print("latency {}".format(time.time() - start_time))
    # print(len(res))


if __name__ == "__main__":
    main()
