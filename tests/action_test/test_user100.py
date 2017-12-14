#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
Module Description
@Time  : 2017/12/14 14：23
@Author: fengweiqian
"""
import random
from tests.action_test.sanic_post import post_http

data_100 = {
        "JWT": "%.24f" % random.random(),
        "email": "1102hfg4@qq.com",
        "password": "123456",
        "superRole": True,
        "ActionId": 100}



if __name__=='__main__':
    res = post_http(data_100)
    print(res)