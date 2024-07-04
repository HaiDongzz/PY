#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/24 15:36
# @Author  : HD
# @File    : WY-TransForms.py
# @Description :

import requests


def save_as_html(url, filename):
    response = requests.get(url)

    with open(filename, 'w', encoding='utf-8') as file:
        file.write(response.text)

    print(f"网页已保存为：{filename}")


# 示例用法
url = "https://v.xiumi.us/board/v5/6pU6n/474280108?in_preview=true&preview_for=normal&stage_ticket=mfGqfbXPLqXNuHhBeh62yAvYk8JAeIDSwCAPNHWWs3qEom76tlguB4fPE0Gk&color_scheme=light"  # 替换为你要保存的网页链接
filename = "定了！8月26日12点！ 温州轨道交通S2线开通运营"  # 替换为你想给保存的HTML文件起的名字
save_as_html(url, filename)
