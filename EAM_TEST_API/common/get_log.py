#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/1 15:42
# @Author  : HD
# @File    : get_log.py
# @Description :

import sys

sys.path.append(r"D:\PyCharm202133\work-space\EAM_TEST_API")
import logging.config
import logging


# 读取日志配置文件
def get_log():
    con_log = "../configs/log.conf"
    logging.config.fileConfig(con_log)
    log = logging.getLogger()
    return log
