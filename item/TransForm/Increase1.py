#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/8/23 9:31
# @Author  : HD
# @File    : Increase1.py
# @Description :

from sqlalchemy import create_engine

# 创建数据库引擎
engine = create_engine('oracle+cx_oracle://t_psmdb:Wzmtr@123456@10.11.76.40:1521/gisdb')

# 建立数据库连接
conn = engine.connect()

# 执行 SQL 查询
result = conn.execute("SELECT * FROM T_PSMDB.T_BUS_SITE_MY")

# 处理查询结果
for row in result:
    print(row)

# 关闭数据库连接
conn.close()
