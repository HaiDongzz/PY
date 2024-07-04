#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/6/28 19:37
# @Author  : HD
# @File    : data.py
# @Description :

import pandas as pd


def read_excel(file, **kwargs):
    data_dict = []
    try:
        data = pd.read_excel(file, engine='openpyxl', **kwargs)
        data_dict = data.to_dict('records')
    except Exception as e:
        print(f"读取Excel文件时出错：{e}")
    finally:
        return data_dict


sheet1 = read_excel('T_data.xlsx')
sheet2 = read_excel('T_data.xlsx', sheet_name='Sheet2')
print("sheet1:")
print(sheet1)
print("============分===========隔============线============")
print("sheet2:")
print(sheet2)

# 向列表中添加一列
data = pd.read_excel('T_data.xlsx', engine='openpyxl')
data['sign'] = data["req.from"] + 'aaaa.' + data["req.to"]
data_dict = data.to_dict('records')
print(data_dict)
