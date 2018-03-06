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
        "email": "110fssdad2sd3@qq.com",
        "password": "123456",
        "superRole": True,
        "ActionId": 100}

data_101 = {
        "JWT": "%.24f" % random.random(),
        "email": "qwer@qq.com",
        "password": "123456",
        "ActionId": 101}

if __name__=='__main__':
    res = post_http(data_101)
    print(res)