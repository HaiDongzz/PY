#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/27 19:55
# @Author  : HD
# @File    : Wzmtr_WZGD_App.py
# @Description :

# 导入webdriver
import time

from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# 初始化参数
desired_caps = {
    'platformName': 'Android',  # 被测手机是安卓
    'platformVersion': '12',  # 手机安卓版本
    'deviceName': 'HuaWei',  # 设备名，安卓手机可以随意填写
    'appPackage': 'org.neusoft.wzmetro.ckfw',  # 启动APP Package名称
    'appActivity': '.app.MainActivity',  # 启动Activity名称
    'unicodeKeyboard': True,  # 使用自带输入法，输入中文时填True
    'resetKeyboard': True,  # 执行完程序恢复原来输入法
    'noReset': True,  # 不要重置App，如果为False的话，执行完脚本后，app的数据会清空，比如你原本登录了，执行完脚本后就退出登录了
    'newCommandTimeout': 6000,
    'automationName': 'UiAutomator2'
}
# 连接Appium Server，初始化自动化环境
driver = webdriver.Remote(" http://127.0.0.1:4723", desired_caps)

driver.find_element(by=AppiumBy.ID, value="et_account").set_text("test@admin.com")
driver.find_element(by=AppiumBy.ID, value="et_pwd").set_text("test 123456")
driver.find_element(by=AppiumBy.ID, value="btn_login").click()

# 停止10s
time.sleep(10)

# 退出程序，记得之前没敲这段报了一个错误 Error: socket hang up 啥啥啥的忘记了，有兴趣可以try one try
# driver.quit()
