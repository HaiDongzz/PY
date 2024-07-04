#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/3/8 15:38
# @Author  : HD
# @File    : Api_request.py
# @Description :

import requests

from Yapi_config import YAPI_URL, TOKEN


# 发送请求
def sent_get_request(url):
    headers = {"Authorization": TOKEN}
    response = requests.get(YAPI_URL + url, headers=headers)
    response = requests.get(url)
    # 检查是否缺少协议信息，如果缺少则添加默认的 https://
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'https://' + url

    response = requests.get(url)

    if response.status_code == 200:
        try:
            # 尝试解析 JSON 数据
            return response.json()
        except ValueError as e:
            print(f"Error decoding JSON: {e}")
            return None
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None
    return response.json()


# post请求
def sent_post_request(url, data):
    headers = {"Authorization": TOKEN}
    response = requests.post(YAPI_URL + url, headers=headers, json=data)
