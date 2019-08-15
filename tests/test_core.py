# !/user/bin/env python
# coding:utf-8
import requests

class ApiHttpbinGet:
    url = "https://httpbin.org/get"
    method = "GET"
    headers = {"accept": "application/json"}

    def run(self):
        self.response = requests.get(self.url,headers=self.headers)
        return self

    def validate(self,key,expected_value):
        value = self.response
        for _key in key.split("."):
            if isinstance(value,requests.Response):
                value = getattr(value, _key)
            elif isinstance(value,requests.structures.CaseInsensitiveDict):
                value = value[_key]
        assert expected_value == value
        return self


class ApiHttpbinPost:
    url = 'https://httpbin.org/post'
    method = "POST"
    json = {'abc': 123}
    headers = {"accept": "application/json"}




def test_version():
    from hogwarts_apitest import __version__
    print("test coverall")
    assert  isinstance(__version__,str)

def test_httpbin_get():
    # resp = requests.get(
    #     'https://httpbin.org/get',
    #     headers={"accept": "application/json"}
    # )
    #
    # assert resp.status_code == 200
    # assert resp.headers["server"] == 'nginx'
    # assert resp.json()["url"] == "https://httpbin.org/get"
    ApiHttpbinGet().run()\
        .validate("status_code",200)\
        .validate("headers.server","nginx")\
        # .validate("json.url","https://httpbin.org/get")


def test_httpbin_get_with_params():
    resp = requests.get(
        'https://httpbin.org/get',
        params={'abc':123},
        headers={"accept": "application/json"}
    )

    assert resp.status_code == 200
    assert resp.headers["server"] == 'nginx'
    assert resp.json()["url"] == "https://httpbin.org/get?abc=123"

def test_httpbin_post():
    resp = requests.post(
        'https://httpbin.org/post',
        # data={'abc':123},
        json={'abc':123},
        headers={"accept": "application/json"}
    )

    assert resp.status_code == 200
    assert resp.json()["url"] ==  "https://httpbin.org/post"
    assert resp.json()["json"]["abc"]== 123