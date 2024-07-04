#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/23 9:48
# @Author  : HD
# @File    : myscript.py
# @Description :

import cx_Oracle

# 连接数据库
dsn = cx_Oracle.makedsn('10.11.76.40', 1521, 'gisdb')
conn = cx_Oracle.connect('t_psmdb', 'Wzmtr@123456', dsn)

# 创建游标
cursor = conn.cursor()

# 执行SQL查询
cursor.execute('SELECT * FROM T_PSMDB.T_BUS_SITE_MY')

# 获取查询结果
result = cursor.fetchall()
for row in result:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()
