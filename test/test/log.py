#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/22 11:01 PM
# @Author  : Agonsle
# @Site    : 
# @File    : log.py
# @Software: PyCharm


import logging

# 打印日志级别
def test_logging():
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')

test_logging()