#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/2 8:47
# @Author  : HD
# @File    : dom.py
# @Description :


# page_url = 'http://192.168.30.140:8199/#/login'
from selenium.webdriver.common.by import By

page_url = 'https://www.jd.com'

elements = [
    {'name': 'search_ipt', 'desc': '搜索框点击', 'by': (By.ID, u'key'), 'ec': 'presence_of_element_located',
     'action': 'send_keys()'},
    {'name': 'search_btn', 'desc': '搜索按钮点击', 'by': (By.CLASS_NAME, u'button'), 'ec': 'presence_of_element_located',
     'action': 'click()'},
]

page_url1 = 'https://search.jd.com/'

elements1 = [
    {'name': 'result_list', 'desc': '结果列表', 'by': (By.CLASS_NAME, u'gl-item'), 'ec': 'presence_of_all_elements_located',
     'action': None},
    {'name': 'price', 'desc': '价格', 'by': (By.XPATH, u".//div[@class='p-price']/strong/i"),
     'ec': 'presence_of_element_located', 'action': 'text'},
    {'name': 'pname', 'desc': '描述', 'by': (By.XPATH, u".//div[@class='p-name p-name-type-2']/a/em"),
     'ec': 'presence_of_element_located', 'action': 'text'}
]
