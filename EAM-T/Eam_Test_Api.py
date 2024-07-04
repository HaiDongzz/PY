#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 9:28
# @Author  : HD
# @File    : Eam_Test_Api.py
# @Description :

import unittest

import HTMLTestRunner
import requests

API_URL_BASE = "http://192.168.30.153:8002/eam"
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhZG1pbiIsInN1YiI6Iuezu-e7n-" \
        "euoeeQhuWRmCIsIkNVUlJFTlRfVVNFUl9JTkZPI" \
        "joie1wiY29tcGFueUlkXCI6XCJBXCIsXCJjb21wYW55TmFtZVwiOlwi6ZuG5Zui5pys57qn" \
        "XCIsXCJvZmZpY2VJZFwiOlwiQTAyXCIsXCJvZmZpY2VOYW1lXCI6XCLlip7lhazlrqRcIixcInBlcn" \
        "NvbklkXCI6XCJhZG1pblwiLFwicGVyc29uTmFtZVwiOlwi57O757uf566h55CG5ZGYXCIsXCJwZXJzb25Ob1wiOlwi" \
        "YWRtaW5cIn0iLCJpYXQiOjE2OTgzNzIyNjMsImV4cCI6MTY5ODk3NzA2M30.-EXChU5JgvjxV8Rrj3tmQmilR6lMRVn0qu2EkLoEF7c"


class ApiTester(unittest.TestCase):
    def setUp(self):
        self.api_url_base = API_URL_BASE
        self.token = TOKEN
        self.headers = {'Authorization': 'Bearer ' + self.token}

    def fetch_all_endpoints(self):
        response = requests.get(self.api_url_base + "/v2/api-docs")
        response.raise_for_status()
        swagger = response.json()

        paths = swagger.get("paths", {})
        return list(paths.keys())

    def call_endpoint(self, endpoint):
        response = requests.get(self.api_url_base + endpoint, headers=self.headers)
        print(response.json())
        return response

    def test_all_endpoints(self):
        endpoints = self.fetch_all_endpoints()
        for endpoint in endpoints:
            response = self.call_endpoint(endpoint)
            if response is None:
                self.fail(f"Endpoint {endpoint} returned no response")
            if response.status_code == 400:
                self.fail(f"Endpoint {endpoint} failed with status code 400")
                print(response.json())  # 打印响应内容
            # 处理其他响应码的情况


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ApiTester)
    with open('test_report.html', 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title='API Test Report')
        runner.run(suite)
