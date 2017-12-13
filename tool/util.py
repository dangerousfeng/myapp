#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 12/12/17 4:06 AM
@Author  : fengweiqian
"""
import datetime
from tool.times import datetime2str
import uuid


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


def get_uuid():
    s_uuid = str(uuid.uuid1())
    l_uuid = s_uuid.split('-')
    s_uuid = ''.join(l_uuid)
    return s_uuid
