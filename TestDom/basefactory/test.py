#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 14:41
# @Author  : HD
# @File    : test.py.py
# @Description :


import os
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from common.getfiledir import SCREENSHOTDIR


class WebdriverOperator(object):

    def __init__(self, driver: Chrome):
        self.driver = driver

    def get_screenshot_as_file(self):
        """
        截屏保存
        :return:返回路径
        """
        pic_name = str.split(str(time.time()), '.')[0] + str.split(str(time.time()), '.')[1] + '.png'
        screent_path = os.path.join(SCREENSHOTDIR, pic_name)
        self.driver.get_screenshot_as_file(screent_path)
        return screent_path

    def gotosleep(self, **kwargs):
        time.sleep(3)
        return True, '等待成功'

    def web_implicitly_wait(self, **kwargs):
        """
        隐式等待
        :return:
        type  存时间
        """
        try:
            s = kwargs['time']
        except KeyError:
            s = 10
        try:
            self.driver.implicitly_wait(s)
        except NoSuchElementException:
            return False, '隐式等待 页面元素未加载完成'
        return True, '隐式等待 元素加载完成'

    def web_element_wait(self, **kwargs):
        """
        等待元素可见
        :return:
        """
        try:
            type = kwargs['type']
            locator = kwargs['locator']
        except KeyError:
            return False, '未传需要等待元素的定位参数'
        try:
            s = kwargs['time']
            if s is None:
                s = 30
        except KeyError:
            s = 30

        try:
            if type == 'id':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.ID, locator)))
            elif type == 'name':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.NAME, locator)))
            elif type == 'class':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.CLASS_NAME, locator)))
            elif type == 'xpath':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.XPATH, locator)))
            elif type == 'css':
                WebDriverWait(self.driver, s, 0.5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            else:
                return False, '不能识别元素类型[' + type + ']'
        except TimeoutException:
            screenshot_path = self.get_screenshot_as_file()
            return False, '元素[' + locator + ']等待出现失败,已截图[' + screenshot_path + '].'
        return True, '元素[' + locator + ']等待出现成功'

    def find_element(self, type, locator, index=None):
        """
        定位元素
        :param type:
        :param itor:
        :param index:
        :return:
        """
        time.sleep(1)
        # isinstance(self.driver, selenium.webdriver.Chrome.)
        if index is None:
            index = 0
        type = str.lower(type)
        try:
            if type == 'id':
                elem = self.driver.find_elements_by_id(locator)[index]
            elif type == 'name':
                elem = self.driver.find_elements_by_name(locator)[index]
            elif type == 'class':
                elem = self.driver.find_elements_by_class_name(locator)[index]
            elif type == 'xpath':
                elem = self.driver.find_elements_by_xpath(locator)[index]
            elif type == 'css':
                elem = self.driver.find_elements_by_css_selector(locator)[index]
            else:
                return False, '不能识别元素类型:[' + type + ']'
        except Exception as e:
            screenshot_path = self.get_screenshot_as_file()
            return False, '获取[' + type + ']元素[' + locator + ']失败,已截图[' + screenshot_path + '].'
        return True, elem

    def element_click(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        try:
            type = kwargs['type']
            locator = kwargs['locator']

        except KeyError:
            return False, '缺少传参'
        try:
            index = kwargs['index']
        except KeyError:
            index = 0
        isOK, result = self.find_element(type, locator, index)
        if not isOK:  # 元素没找到，返回失败结果
            return isOK, result
        elem = result
        try:
            elem.click()
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            return False, '元素[' + locator + ']点击失败,已截图[' + screenshot_path + '].'
        return True, '元素[' + locator + ']点击成功'

    def element_input(self, **kwargs):
        """

        :param kwargs:
        :return:
        """
        try:
            type = kwargs['type']
            locator = kwargs['locator']
            text = str(kwargs['input'])
        except KeyError:
            return False, '缺少传参'
        try:
            index = kwargs['index']
        except KeyError:
            index = 0
        isOK, result = self.find_element(type, locator, index)
        if not isOK:  # 元素没找到，返回失败结果
            return isOK, result
        elem = result
        try:
            elem.send_keys(text)
        except Exception:
            screenshot_path = self.get_screenshot_as_file()
            return False, '元素[' + locator + ']输入[' + text + ']失败,已截图[' + screenshot_path + '].'
        return True, '元素[' + locator + ']输入[' + text + ']成功'
