# !/user/bin/env python
# coding:utf-8
from hogwarts_apitest.api import BaseAPI


class ApiHttpbinGet(BaseAPI):
    url = "https://httpbin.org/get"
    method = "GET"
    headers = {"accept": "application/json"}
    params ={}

class ApiHttpbinPost(BaseAPI):
    url = 'https://httpbin.org/post'
    method = "POST"
    json = {'abc': 123}
    headers = {"accept": "application/json"}
