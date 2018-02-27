#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 12/12/17 4:06 AM
@Author  : fengweiqian
"""
import datetime
from tool.times import datetime2str
import shortuuid


def asDict(obj):
    res = {}
    obj_dict = obj.__dict__
    __data = obj_dict["_data"]
    for k, v in __data.items():
        value = v
        if isinstance(v, datetime.datetime):
            value = datetime2str(v)
        res[k] = value
    return res

def field_to_hump(field_name):
    """
    role_name > roleName
    小写加下划线转驼峰命名法
    :param field_name:
    :return:
    """
    string_list = str(field_name).split("_")
    first = string_list[0].lower()
    others = string_list[1:]
    others_capital = [word.capitalize() for word in others]
    others_capital[0:0] = [first]
    return ''.join(others_capital)

def get_uuid():
    uuid = shortuuid.uuid()
    return uuid

