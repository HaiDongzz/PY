#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 14:56
# @Author  : HD
# @File    : getcase.py
# @Description : 读取用例


import os

import openpyxl

from common.getfiledir import DATADIR

file = os.path.join(DATADIR, 'case.xlsx')


class ReadCase(object):
    def __init__(self):
        self.sw = openpyxl.load_workbook(file)
        print(self.sw)

    def openxlsx(self, file):
        """
        打开文件
        :param dir:
        :return:
        """
        # self.sw = openpyxl.load_workbook(file)

    # [{"a": [{"A": 2}, {"A": 2}, {"A": 2}, {"A": 2}, {"A": 2}, {"A": 2}, {"A": 2}, {"A": 2}, {"A": 2}]},{"a": [5, 3, 2]}, {"a": [10, 4, 6]}]
    def readallcase(self):
        """
        取所有sheet页
        :return:list,返回sheet页里的数据
        """
        sheet_list = []
        for sh in self.sw:
            if 'common' != sh.title.split('_')[0] and 'common' != sh.title.split('-')[0] and sh.title[0] is not '#':
                isOK, result = self.readcase(sh)
                if isOK:
                    sheet_list.append(result)
        if sheet_list is None:
            return False, '用例集是空的，请检查用例'
        return True, sheet_list

    def readcase(self, sh):
        """
        组合sheet页的数据
        :param sh:
        :return: list,返回组合数据
        """
        if sh is None:
            print('sheet页为空')
        datas = list(sh.rows)
        if datas == []:
            return False, '用例[' + sh.title + ']里面是空的'
        title = [i.value for i in datas[0]]
        rows = []
        sh_dict = {}
        for i in datas[1:]:
            data = [v.value for v in i]
            row = dict(zip(title, data))
            try:
                if str(row['id'])[0] is not '#':
                    row['sheet'] = sh.title
                    rows.append(row)
            except KeyError:
                raise e
                rows.append(row)
            sh_dict[sh.title] = rows
        return True, sh_dict

    def get_common_case(self, case_name):
        """
        得到公共用例
        :param case_name:
        :return:
        """
        try:
            sh = self.sw.get_sheet_by_name(case_name)
        except KeyError:
            return False, '未找到公共用例[' + case_name + '],请检查用例'
        except DeprecationWarning:
            pass
        return self.readcase(sh)
