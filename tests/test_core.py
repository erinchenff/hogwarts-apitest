# !/user/bin/env python
# coding:utf-8
import requests

from hogwarts_apitest.api import BaseAPI

def test_version():
    from hogwarts_apitest import __version__
    assert isinstance(__version__,str)

class ApiHttpbinGet(BaseAPI):
    url = "https://httpbin.org/get"
    method = "GET"
    headers = {"accept": "application/json"}
    params ={}


def test_httpbin_get():
    ApiHttpbinGet().run()\
        .validate("status_code",200)\
        .validate("headers.server","nginx")\
        .validate("json().url","https://httpbin.org/get")\
        .validate("json().headers.Accept","application/json")


def test_httpbin_get_with_params():
    ApiHttpbinGet()\
        .set_params(abc=123,xyz=456)\
        .run()\
        .validate("status_code",200)\
        .validate("headers.server",'nginx')\
        .validate("json().url","https://httpbin.org/get?abc=123&xyz=456")


class ApiHttpbinPost(BaseAPI):
    url = 'https://httpbin.org/post'
    method = "POST"
    json = {'abc': 123}
    headers = {"accept": "application/json"}

def test_httpbin_post():
    ApiHttpbinPost()\
        .set_json({'abc': 123})\
        .run()\
        .validate("status_code",200)\
        .validate("url", "https://httpbin.org/post")\
        # .validate("json().abc","123")
