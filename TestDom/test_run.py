#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 15:29
# @Author  : HD
# @File    : test_run.py
# @Description :


import os
import unittest

from common.getfiledir import CASEDIR, REPORTDIR
from library.HTMLTestRunnerNew import HTMLTestRunner


class Test_run(object):

    def __init__(self):
        self.suit = unittest.TestSuite()
        self.load = unittest.TestLoader()
        self.suit.addTest(self.load.discover(CASEDIR))
        self.runner = HTMLTestRunner(
            stream=open(os.path.join(REPORTDIR, 'report.html'), 'wb'),
            title='自动化工厂',
            description='测试数据',
            tester='HUNWEI'
        )

    def excute(self):
        self.runner.run(self.suit)


if __name__ == "__main__":
    test_run = Test_run()
    test_run.excute()
