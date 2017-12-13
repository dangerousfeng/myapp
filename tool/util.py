#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 12/12/17 4:06 AM
@Author  : fengweiqian
"""


def convert_to_dict(obj):
    """
    把Object对象转换成Dict对象
    :param obj:
    :return:
    """
    dict = {}
    dict.update(obj.__dict__)
    return dict