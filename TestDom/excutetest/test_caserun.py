#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 15:27
# @Author  : HD
# @File    : test_caserun.py.py
# @Description :

:::iiimport
unittest

from common.log import mylog

from common.factory import Factory
from library.ddt import ddt, data


@ddt
class Test_caserun(unittest.TestCase):
    fac = Factory()
    isOK, excu_cases = fac.init_execute_case()

    @data(*excu_cases)
    def test_run(self, acases):
        for key, cases in acases.items():
            mylog.info('\n----------用例【%s】开始----------' % cases[0].get('sheet'))
            print('\n')
            for case in cases:
                isOK, result = self.fac.execute_keyword(**case)
                if isOK:
                    print(result)
                    mylog.info(result)
                else:
                    mylog.error(result)
                    raise Exception(result)
            mylog.info('\n----------用例【%s】结束----------\n' % cases[0].get('sheet'))

        for key, cases in acases.items():
            mylog.info('\n----------用例【%s】开始----------' % cases[0].get('sheet'))
            print('\n')
            for case in cases:
                isOK, result = self.fac.execute_keyword(**case)
                if isOK:
                    print(result)
                    mylog.info(result)
                else:
                    mylog.error(result)
                    raise Exception(result)
            mylog.info('\n----------用例【%s】结束----------\n' % cases[0].get('sheet'))
