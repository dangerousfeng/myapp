#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description:
@Time    : 2017/12/11 17:02
@Author  : fengweiqian
"""
import requests,json


class TestNetManager(object):
    headers = [{'content-type': 'application/x-www-form-urlencoded'},
               {'content-type': 'application/json;charset=utf-8'},
               {'content-type': 'application/xml;charset=utf-8'}
               ]

    def __init__(self):
        pass

    @classmethod
    def request_server(cls, method, server_url, data, header_index=1):
        # default data is json type
        if method == 'get':
            try:
                r = requests.get(server_url, params=data)
                r.encoding = 'utf-8'
                root = r.content
                return root
            except requests.exceptions.HTTPError:
                return False
        if method == 'post':
            try:
                r = requests.post(server_url, data=data, headers=cls.headers[header_index])
                r.encoding = 'utf-8'
                root = r.content
                return root
            except requests.exceptions.HTTPError:
                return False


if __name__ == '__main__':
    pass
