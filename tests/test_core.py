# !/user/bin/env python
# coding:utf-8

def test_version():
    from hogwarts_apitest import __version__
    print("test coverall")
    assert  isinstance(__version__,str)