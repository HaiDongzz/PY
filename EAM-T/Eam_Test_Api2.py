#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/27 9:57
# @Author  : HD
# @File    : Eam_Test_Api2.py
# @Description :
import pytest
import requests
from pytest_html import extras

API_URL_BASE = "http://192.168.30.153:8002/eam"
TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJhZG1pbiIsInN1YiI6Iuezu-e7n-" \
        "euoeeQhuWRmCIsIkNVUlJFTlRfVVNFUl9JTkZPI" \
        "joie1wiY29tcGFueUlkXCI6XCJBXCIsXCJjb21wYW55TmFtZVwiOlwi6ZuG5Zui5pys57qn" \
        "XCIsXCJvZmZpY2VJZFwiOlwiQTAyXCIsXCJvZmZpY2VOYW1lXCI6XCLlip7lhazlrqRcIixcInBlcn" \
        "NvbklkXCI6XCJhZG1pblwiLFwicGVyc29uTmFtZVwiOlwi57O757uf566h55CG5ZGYXCIsXCJwZXJzb25Ob1wiOlwi" \
        "YWRtaW5cIn0iLCJpYXQiOjE2OTgzNzIyNjMsImV4cCI6MTY5ODk3NzA2M30.-EXChU5JgvjxV8Rrj3tmQmilR6lMRVn0qu2EkLoEF7c"


class ApiTester:
    def __init__(self, api_url_base=API_URL_BASE, token=TOKEN):
        self.api_url_base = api_url_base
        self.token = token
        self.headers = {'Authorization': 'Bearer ' + self.token}

    def fetch_all_endpoints(self):
        '''
        从swagger.json获取所有端点,假设swagger.json在“/swagger.json”端点可用。
        您可以根据API更新此函数来解析swagger.json
        '''
        response = requests.get(self.api_url_base + "/v2/api-docs")
        response.raise_for_status()  # 如果请求失败，此语句将引发HTTPError
        swagger = response.json()

        # 端点在swagger模式的“path”键下可用
        paths = swagger.get("paths", {})
        return list(paths.keys())

    def call_endpoint(self, endpoint):
        '''
        调用单个端点并验证响应
        '''
        response = requests.get(self.api_url_base + endpoint, headers=self.headers)
        assert response.status_code == 200
        print(requests.Request)
        print("=============分割线=======================================")
        print(response.text)
        # 调用单个端点并验证响应


'''
class TestApi:

    def test_all_endpoints(self):
        api_tester = ApiTester(API_URL_BASE, TOKEN)
        endpoints = api_tester.fetch_all_endpoints()
        for endpoint in endpoints:
            response = api_tester.call_endpoint(endpoint)
            if response.status_code == 400:
                print(f"Endpoint{endpoint}failed with status code 400")

            api_tester.call_endpoint(endpoint)
            '''


class TestApi:
    def test_all_endpoints(self):
        api_tester = ApiTester(API_URL_BASE, TOKEN)
        endpoints = api_tester.fetch_all_endpoints()
        for endpoint in endpoints:
            response = api_tester.call_endpoint(endpoint)
            if response is None:
                print(f"Endpoint {endpoint} returned no response")
                continue
            if response.status_code == 400:
                print(f"Endpoint {endpoint} failed with status code 400")
                print(response.json())  # 打印响应内容
                continue
            # 处理其他响应码的情况

    def pytest_html_results_summary(self, prefix, summary, postfix):
        summary.extend([extras.HTML.section(extras.HTML.h2('接口数量统计')),
                        extras.HTML.section(extras.HTML.p(f'接口数量:{len(self.endpopints)}'))])

        # 生成测试报告
        with open("D:\test_report.html", 'w', encoding='utf-8') as file:
            file.write(prefix + ''.join(summary) + postfix)


if __name__ == '__main__':
    pytest.main(['-s', '--html=test_report.html'])
