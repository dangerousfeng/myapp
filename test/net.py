# -*- coding : utf-8 -*-
"""
Created on 2016.10.14

@author: DengShengjin
modify ChenJingYi 2017.3.7
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
