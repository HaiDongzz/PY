#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/24 14:44
# @Author  : HD
# @File    : HtmlDownload.py
# @Description :

import urllib.request

import requests
from bs4 import BeautifulSoup


def download_images(url):
    # 发送HTTP请求获取HTML页面内容
    response = requests.get(url)

    # 解析HTML页面
    soup = BeautifulSoup(response.text, 'html.parser')

    # 查找所有的<img>标签
    img_tags = soup.find_all('img')

    # 逐个下载图片
    for img_tag in img_tags:
        # 获取图片链接
        img_url = img_tag['data-src']

        try:
            # 下载图片
            filename = img_url.split("/")[-1]
            urllib.request.urlretrieve(img_url, filename)
            print("已下载图片:", img_url)
        except Exception as e:
            print("下载图片时出错:", str(e))


# 示例用法
url = "https://mp.weixin.qq.com/s/Dgd-W5cazTpmleINt8wXnA"  # 替换为你要下载图片的网页链接
download_images(url)
