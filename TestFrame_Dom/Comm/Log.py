#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/28 17:06
# @Author  : HD
# @File    : Log.py.py
# @Description :

import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler

from PIL import ImageGrab

from Conf.config import log_cfg

_BaseHome = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

_log_level = eval(log_cfg['log_level'])
_log_path = log_cfg['log_path']
_log_format = log_cfg['log_format']
# 对运行日志做处置，拼接日志
_log_file = os.path.join(_BaseHome, _log_path, 'log.txt')
try:
    with open(_log_file, 'w') as f:
        f.write('Testing write permission.')
    print(f"Successfully wrote to {_log_file}")
except Exception as e:
    print(f"Failed to write to {_log_file}: {e}")


def log_init():
    logger = logging.getLogger('main.jd')
    logger.setLevel(level=_log_level)
    formatter = logging.Formatter(_log_format)

    handler = TimedRotatingFileHandler(filename=_log_file, when='D', interval=1, backupCount=7)
    handler.setLevel(_log_level)
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    console = logging.StreamHandler()
    console.setLevel(_log_level)
    console.setFormatter(formatter)
    logger.addHandler(console)


# 日志截图
_today = time.strftime("%Y%m%d")
_screen_path = os.path.join(_BaseHome, _log_path, 'Screen', _today)


# 使用PIL的ImageGrab进行日志截图
def screen(name):
    t = time.time()
    png = ImageGrab.grab()
    if not os.path.exists(_screen_path):
        os.makedirs(_screen_path)
    image_name = os.path.join(_screen_path, name)
    # 文件明加时间戳，避免重复
    png.save('%s_%s.png' % (image_name, str(round(t * 1000))))


log_init()
logger = logging.getLogger('main.jd')
logger.info('log test ------------------------------------')
