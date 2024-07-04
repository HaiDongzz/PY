#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/14 16:58
# @Author  : HD
# @File    : EIP_APP_Api.py
# @Description :


import datetime
import time

import requests

url = 'https://m.wzmtr.com:7443/eip/mobile/co/oapi/forward'
params = {'appid': 'a4c768b67aa74fa28c7767188cad7ac9'}  # 接口需要的参数

# 设置请求头，包含Authorization字段
headers = {
    'Authorization': 'eyJhbGciOiJIUzI1NiJ9.eyJsb2dpbl90b2tlbl9rZXlfIjoiODBiZj'
                     'FlYjktOGM2NC00MGJkLTljYmMtMTRkZWVkMjE5YTcyIn0.RjkwYX_ObqdiNxPJ8WZmBAtcSUBE7AEemBjMj3oPIq8'}

while True:
    try:
        response = requests.get(url, params=params, headers=headers, timeout=30)  # 发送请求，设置超时时间为30秒
        response.raise_for_status()  # 如果响应状态码不是200，会抛出异常
        with open(r'D:\PyCharm202133\work-space\EIP_ITEM_api\response.txt', 'w', encoding='utf-8') as f:
            f.write(response.text)  # 将响应内容保存到本地文件response.txt中
        print('请求成功，响应内容已保存到response.txt')
    except requests.exceptions.Timeout:
        print('请求超时')
    except requests.exceptions.HTTPError as err:
        with open('error.txt', 'w', encoding='utf-8') as f:
            f.write(str(err))  # 将错误信息保存到本地文件error.txt中
        print('请求报错，错误信息已保存到error.txt')
    except requests.exceptions.RequestException as err:
        with open('error.txt', 'w', encoding='utf-8') as f:
            f.write(str(err))  # 将错误信息保存到本地文件error.txt中
        print('请求发生异常，错误信息已保存到error.txt')
    print(datetime.datetime.now(), response.text)
    # 设置延迟时间，单位为秒
    time.sleep(0.5)  # 每次循环后暂停秒
