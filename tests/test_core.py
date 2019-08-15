# !/user/bin/env python
# coding:utf-8
import requests

from hogwarts_apitest.api import BaseAPI
from tests.api.httpbin import ApiHttpbinGet, ApiHttpbinPost


def test_version():
    from hogwarts_apitest import __version__
    assert isinstance(__version__,str)

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

def test_httpbin_post():
    ApiHttpbinPost()\
        .set_json({"abc": "123"})\
        .run()\
        .validate("status_code",200)\
        .validate("url", "https://httpbin.org/post")\
        .validate("json().json.abc","123")

def test_httpbin_parameters_share():
    user_id = "adk129"
    ApiHttpbinGet()\
        .set_params(user_id=user_id)\
        .run()\
        .validate("status_code",200)\
        .validate("headers.server",'nginx')\
        .validate("json().url","https://httpbin.org/get?user_id={}".format(user_id))

    ApiHttpbinPost()\
        .set_json({"user_id": user_id})\
        .run()\
        .validate("status_code",200)\
        .validate("url", "https://httpbin.org/post")\
        .validate("json().json.user_id", user_id)