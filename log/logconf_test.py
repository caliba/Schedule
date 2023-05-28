#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/28 11:57 AM
# @Author  : Agonsle
# @Site    :
# @File    : logconf_test.py
# @Software: PyCharm
import logging
import logging.config

logging.basicConfig(filemode='w')


logging.config.fileConfig('logging.conf')
root = logging.getLogger()
frontend = logging.getLogger('frontend')
frontend.info("frontend info")
root.debug("root")

logger = logging.getLogger('applog')

logger.debug("applog file")
logger.info("sb ")