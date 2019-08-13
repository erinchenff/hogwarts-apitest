# !/user/bin/env python
# coding:utf-8

def test_version():
    from hogwarts_apitest import __version__
    assert  isinstance(__version__,str)