#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
Module Description
@Time  : 2018/03/06 11：42
@Author: fengweiqian
"""

import random
from tests.action_test.sanic_post import post_http

USER_ID = "cDjikfVvEeafs7JsaiANpg"
JWT = "%.24f" % random.random()

data_202 = {
    "JWT": JWT,
    "userId":USER_ID,
    "ActionId": 202}
data_203 = {
    "JWT": JWT,
    "userId":USER_ID,
    "ActionId": 203,
    "courseId":"saGogHA2ysjFvNBH4eRgcU"
}
data_204 = {
    "JWT": JWT,
    "userId":USER_ID,
    "ActionId": 204,
    "courseId":"saGogHA2ysjFvNBH4eRgcU"
}

if __name__=='__main__':
    res = post_http(data_202)
    print(res)