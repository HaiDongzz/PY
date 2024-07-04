#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 9:24
# @Author  : HD
# @File    : test_dom_desktop.py
# @Description :
import logging
import os
import unittest

import ddt
from selenium import webdriver

from Comm.Log import screen
from Comm.data import read_excel
from Page.basePage import Page
from main import TestCasePath

logger = logging.getLogger('main.dom')

# 读取测试数据
file = os.path.join(TestCasePath, 'CIRB/Testdata/dom/test_dom_desktop.xlsx')
test_data = read_excel(file, engine='openpyxl')

PO_dom = 'Page.dom.dom'
PO_search = 'Page.dom.search_dom'


# 数据驱动
@ddt.ddt
class TestdomSearchDesktop(unittest, Testcase):
    """运营日报搜索测试"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.count = 0
        self.result = []

    # 数据驱动传的具体参数
    @ddt.data(*test_data)
    def testdomSearchDesktop(self, test_data):
        """运营日报--车辆部---搜索"""
        url = 'https://www.jd.com'
        keyword = test_data['keword']
        wait = self.driver.implictitly_wait(5)

        try:
            self.driver.get(url)
            # 实例化运营日报主页面
            dom = Page(self.driver, PO_dom)
            # 实例化运营日报的搜索结果
            dom_search = Page(self.driver, PO_search)
            wait
            # 运营日报主页面搜索框输入关键字
            dom.oper_elem('search_ipt', keyword)
            wait
            # 操作运营日报页面的搜索按钮元素
            dom.oper_elem('search_btn')

            time.sleep(3)
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
            time.sleep(2)

            # 运营提报--车辆部日报搜索结果列表
            lis = dom_search.oper_elem('result_list')

            # 在取到的结果存入excel
            for each in lis:
                self.count += 1
                page_each = Page(each, PO_search)
                price = page_each.oper_elem('price')
                name = page_each.oper_elem('panme')
                self.result.append([name, price])

            time.sleep(2)

        except Exception as E:
            logger.error('error info: %s' % (E))
            screen(test_data['keyword'])

        # 数量判断
        self.assertEqual(test_data['count'], self.count)

    def tearDown(self):
        self.driver.quit()
