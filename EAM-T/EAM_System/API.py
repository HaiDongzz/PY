#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/16 15:38
# @Author  : HD
# @File    : API.py
# @Description :


import requests

# 定义接口请求的URL和参数
url = "http://192.168.30.153:8002/eam/basic/region/add"
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhZG1pbiIsInN1YiI6Iuezu-e7n-" \
        "euoeeQhuWRmCIsIkNVUlJFTlRfVVNFUl9JTkZPI" \
        "joie1wiY29tcGFueUlkXCI6XCJBXCIsXCJjb21wYW55TmFtZVwiOlwi6ZuG5Zui5pys57qn" \
        "XCIsXCJvZmZpY2VJZFwiOlwiQTAyXCIsXCJvZmZpY2VOYW1lXCI6XCLlip7lhazlrqRcIixcInBlcn" \
        "NvbklkXCI6XCJhZG1pblwiLFwicGVyc29uTmFtZVwiOlwi57O757uf566h55CG5ZGYXCIsXCJwZXJzb25Ob1wiOlwi" \
        "YWRtaW5cIn0iLCJpYXQiOjE2OTgzNzIyNjMsImV4cCI6MTY5ODk3NzA2M30.-EXChU5JgvjxV8Rrj3tmQmilR6lMRVn0qu2EkLoEF7c"
headers = {
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Authorization": TOKEN
}

data = {
    "lineCode": "01",
    "nodeCode": "0101",
    "nodeLevel": 0,
    "nodeName": "接口导入新增",
    "parentNodeRecId": "0",
    "recCreateTime": "2023-11-16 16:00:00",
    "recCreator": "DHD",
    "recId": "1",
    "recReviseTime": "2023-11-16 16:00:00",
    "recRevisor": "dhd",
    "recStatus": "10",
    "remark": "测试数据"
}

# 发送POST请求
response = requests.post(url, headers=headers, json=data)
print(data)

# 解析响应结果
status_code = response.status_code
json_data = response.json()

# 打印响应状态码和返回数据
print("Status Code:", status_code)
print("Response:", json_data)
