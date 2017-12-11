#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/22 17:34
# @Author  : Fengweiqian
# @File    : sanic_post.py
import json
import random
import requests

session_http_url = "http://127.0.0.1:5000/mooc"
c_pub = '-----BEGIN PUBLIC KEY-----\nMIIBSzCCAQMGByqGSM49AgEwgfcCAQEwLAYHKoZIzj0BAQIhAP////8AAAABAAAA\nAAAAAAAAAAAA////////////////MFsEIP////8AAAABAAAAAAAAAAAAAAAA////\n///////////8BCBaxjXYqjqT57PrvVV2mIa8ZR0GsMxTsPY7zjw J9JgSwMVAMSd\nNgiG5wSTamZ44ROdJreBn36QBEEEaxfR8uEsQkf4vOblY6RA8ncDfYEt6zOg9KE5\nRdiYwpZP40Li/hp/m47n60p8D54WK84zV2sxXs7LtkBoN79R9QIhAP////8AAAAA\n////////// 85vqtpxeehPO5ysL8YyVRAgEBA0IABEhHpxajhmAY8E7u3BhM8SL/\n1yCdAq4RbpGDske9JnK0WfplR7Wc4FyZRghWKwJVf5JUWPLuwWP6HarOxMQlquU=\n-----END PUBLIC KEY-----\n'
headers = [{'content-type': 'application/x-www-form-urlencoded'},
               {'content-type': 'application/json;charset=utf-8'},
               {'content-type': 'application/xml;charset=utf-8'}
               ]


def post_http():

    data = {
            "JWT": "%.24f" % random.random(),
            "Key": "%.20f" % random.random(),
            "c_pub": c_pub,
            "ActionId":20000}
    action_data = json.dumps(data).encode('utf8')
    r = requests.post(session_http_url, data=action_data ,headers=headers[2])
    print (r.json())





if __name__ == '__main__':
    post_http()