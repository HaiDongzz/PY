#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/1 15:42
# @Author  : HD
# @File    : base.py
# @Description :

import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + ".")
sys.path.append(rootPath)
