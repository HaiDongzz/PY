#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 14:54
# @Author  : HD
# @File    : EAM_Api.py
# @Description :


import json
import unittest

import HTMLTestRunner
import pandas as pd
import requests

df = pd.read_excel('D:\PyCharm202133\work-space\EAM-T\EAM_System\params.xlsx', sheet_name='Sheet1')
params1 = df.iloc[0].to_dict()


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://192.168.30.153:8002/eam/v2/api-docs"  # 系统B的地址
        self.token = "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhZG1pbiIsInN1YiI6Iuezu-e7n-" \
                     "euoeeQhuWRmCIsIkNVUlJFTlRfVVNFUl9JTkZPIjoie1wiY29tcGFueUlkXCI6XCJBXCIsXCJ" \
                     "jb21wYW55TmFtZVwiOlwi6ZuG5Zui5pys57qnXCIsXCJvZmZpY2VJZFwiOlwiQTAyXCIsXCJvZmZp" \
                     "Y2VOYW1lXCI6XCLlip7lhazlrqRcIixcInBlcnNvbklkXCI6XCJhZG1pblwiLFwicGVyc29uTmFtZVwiOl" \
                     "wi57O757uf566h55CG5ZGYXCIsXCJwZXJzb25Ob1wiOlwiYWRtaW5cIn0iLCJpYXQiOjE2OTg3NDMxMDgsImV4cCI6" \
                     "MTY5OTM0NzkwOH0.e9zEOCQy2tYNU5Mv1MZfhWpozf-emSXPGC-NkZUM5d8"  # 接口请求需要的固定token

    def test_api_Eam(self):
        url = self.base_url + ""
        headers = {"Authorization": "Bearer " + self.token}
        params1 = {
            "lineCode": "string",
            "nodeCode": "string",
            "nodeLevel": 0,
            "nodeName": "string",
            "parentNodeRecId": "string",
            "recCreateTime": "string",
            "recCreator": "string",
            "recId": "string",
            "recReviseTime": "string",
            "recRevisor": "string",
            "recStatus": "string",
            "remark": "string"
        }

        response = requests.get(url, headers=headers, params=params1)
        result = json.dumps(response.json(), indent=4)
        print(result)
        # 打开文件，使用 'w' 模式表示写入模式
        result_file = open("D:\PyCharm202133\work-space\EAM-T\EAM_System\EAM_API.txt", "w")

        # 将结果写入文件
        result_file.write(result)

        # 关闭文件
        result_file.close()

        self.assertEqual(response.status_code, 200)  # 断言状态码为200

        # self.assertIn('code',result)    #检查响应结果中是否存在code
        # self.assertEqual(result['code'], 401)  # 断言返回的code字段为0
        # self.assertIn('success',response.json())

        # 进一步根据接口的返回结果进行断言和验证

    def tearDown(self):
        pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(APITestCase("test_api_EAM"))

    # 定义报告存放路径
    report_path = "test_report.html"
    fp = open("D:\PyCharm202133\work-space\EAM-T\EAM_System", "wb")

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="API Test Report", description="Test Result")
    runner.run(suite)
    # fp.close()
