#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 14:49
# @Author  : HD
# @File    : getfiledir.py
# @Description :读取取框架各目录的绝对路径

import os

dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(dir)
DATADIR = os.path.join(dir, 'data')
# print(DATADIR)
CONFDIR = os.path.join(dir, 'config')
# print(CONFDIR)
BASEFACTORYDIR = os.path.join(dir, 'basefactory')
# print(BASEFACTORYDIR)
RESULTDIR = os.path.join(dir, 'result')
# print(RESULTDIR)
LOGDIR = os.path.join(RESULTDIR, 'log')
# print(LOGDIR)
REPORTDIR = os.path.join(RESULTDIR, 'report')
# print(REPORTDIR)
SCREENSHOTDIR = os.path.join(RESULTDIR, 'screenshot')
# print(SCREENSHOTDIR)
CASEDIR = os.path.join(dir, 'excutetest')
# print(CASEDIR)

# print(SCREENSHOTDIR)
