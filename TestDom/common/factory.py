#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 15:17
# @Author  : HD
# @File    : factory.py
# @Description :


from basefactory.browseroperator import BrowserOperator
from basefactory.webdriveroperator import WebdriverOperator
from common.getcase import ReadCase
from common.getconf import Config


class Factory(object):

    def __init__(self):
        self.con = Config()
        self.con_fun = dict(self.con.items('Function'))

        """
        浏览器操作对象
        """
        self.browser_opr = BrowserOperator()
        """
        网页操作对象
        """
        self.webdriver_opr = None

    def init_webdriver_opr(self, driver):
        self.webdriver_opr = WebdriverOperator(driver)

    def get_base_function(self, function_name):
        try:
            function = getattr(self.browser_opr, function_name)
        except Exception:
            try:
                function = getattr(self.webdriver_opr, function_name)
            except Exception:
                return False, '未找到注册方法[' + function_name + ']所对应的执行函数，请检查配置文件'
        return True, function

    def execute_keyword(self, **kwargs):
        """
        工厂函数，用例执行方法的入口
        :param kwargs:
        :return:
        """
        try:
            keyword = kwargs['keyword']
            if keyword is None:
                return False, '没有keyword，请检查用例'
        except KeyError:
            return False, '没有keyword，请检查用例'

        _isbrowser = False

        try:
            function_name = self.con_fun[keyword]
        except KeyError:
            return False, '方法Key[' + keyword + ']未注册，请检查用例'

        # 获取基础类方法
        isOK, result = self.get_base_function(function_name)
        if isOK:
            function = result
        else:
            return isOK, result

        # 执行基础方法，如打网点页、点击、定位、隐式等待 等
        isOK, result = function(**kwargs)

        # 如果是打开网页，是浏览器初始化，需要将返回值传递给另一个基础类
        if '打开网页' == keyword and isOK:
            url = kwargs['locator']
            self.init_webdriver_opr(result)
            return isOK, '网页[' + url + ']打开成功'
        return isOK, result

    def init_common_case(self, cases):
        """
        :param kwargs:
        :return:
        """
        cases_len = len(cases)
        index = 0
        for case in cases:
            if case['keyword'] == '调用用例':
                xlsx = ReadCase()
                try:
                    case_name = case['locator']
                except KeyError:
                    return False, '调用用例没提供用例名，请检查用例'
                isOK, result = xlsx.get_common_case(case_name)
                if isOK and type([]) == type(result):
                    isOK, result_1 = self.init_common_case(result)  # 递归检查公共用例里是否存在调用用例
                elif not isOK:
                    return isOK, result
                list_rows = result[case_name]
                cases[index: index + 1] = list_rows  # 将公共用例插入到执行用例中去
            index += 1
        if cases_len == index:
            return False, ''
        return True, cases

    # [{"a": [{"A": 2}, {"A": 2}, {"A": 2}, {"A": 2}, {"A": 2}, {"A": 2}, {"A": 2}, {"A": 2}, {"A": 2}]},{"a": [5, 3, 2]}, {"a": [10, 4, 6]}]

    def init_execute_case(self):
        print("----------初始化用例----------")
        xlsx = ReadCase()
        isOK, result = xlsx.readallcase()
        if not isOK:
            print(result)
            print("----------结束执行----------")
            exit()
        all_cases = result
        excu_cases = []
        for cases_dict in all_cases:
            for key, cases in cases_dict.items():
                isOK, result = self.init_common_case(cases)
                if isOK:
                    cases_dict[key] = result
                else:
                    cases_dict[key] = cases
                excu_cases.append(cases_dict)
                print("----------初始化用例完成----------")
        return excu_cases
