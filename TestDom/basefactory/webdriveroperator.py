#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/7/4 15:48
# @Author  : HD
# @File    : webdriveroperator.py
# @Description :

wd = BrowserOperator()
isOK, deiver = wd.open_url(locator='https://www.qq.com')
time.sleep(5)
deiver.find_elements_by_xpath('//*[@id="sougouTxt"]')[0].send_keys('飞人')
deiver.find_elements_by_xpath('//*[@id="searchBtn"]')[0].click()
