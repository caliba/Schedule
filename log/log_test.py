#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2023/5/28 11:57 AM
# @Author  : Agonsle
# @Site    : 
# @File    : log_test.py
# @Software: PyCharm

import logging

# DEBUG -> INFO -> WARNING -> ERROR

# 记录器 不写，等级默认是warning
logger = logging.getLogger("Applog")
logger.setLevel(logging.DEBUG)

# 处理器 ,处理器与记录器level取最高的
consoleHanler = logging.StreamHandler()
consoleHanler.setLevel(logging.DEBUG)

# 未指定日志级别，将使用handler的级别
fileHandler = logging.FileHandler(filename="tmp1.log")

# 给处理器设置格式
formatter = logging.Formatter('%(asctime)-15s\t|%(threadName)s %(message)s')
consoleHanler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 记录器设置处理器
logger.addHandler(consoleHanler)
logger.addHandler(fileHandler)

# 定义过滤器
filter = logging.Filter("cn.cbb") # 根据logger名字判断
# 关联过滤器
# logger.addFilter()


# 记录器
logger.info("info")
logger.debug("debug")
logger.error("error")
logger.warning("warning")

