#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description:
@Time    : 2017/12/11 17:02
@Author  : fengweiqian
"""
import json
import requests

session_http_url = "http://127.0.0.1:5000/mooc"
#session_http_url = "http://www.fengweiqian.tech:5000/mooc"
c_pub = '-----BEGIN PUBLIC KEY-----\nMIIBSzCCAQMGByqGSM49AgEwgfcCAQEwLAYHKoZIzj0BAQIhAP////8AAAABAAAA\nAAAAAAAAAAAA////////////////MFsEIP////8AAAABAAAAAAAAAAAAAAAA////\n///////////8BCBaxjXYqjqT57PrvVV2mIa8ZR0GsMxTsPY7zjw J9JgSwMVAMSd\nNgiG5wSTamZ44ROdJreBn36QBEEEaxfR8uEsQkf4vOblY6RA8ncDfYEt6zOg9KE5\nRdiYwpZP40Li/hp/m47n60p8D54WK84zV2sxXs7LtkBoN79R9QIhAP////8AAAAA\n////////// 85vqtpxeehPO5ysL8YyVRAgEBA0IABEhHpxajhmAY8E7u3BhM8SL/\n1yCdAq4RbpGDske9JnK0WfplR7Wc4FyZRghWKwJVf5JUWPLuwWP6HarOxMQlquU=\n-----END PUBLIC KEY-----\n'
headers = [{'content-type': 'application/x-www-form-urlencoded'},
               {'content-type': 'application/json;charset=utf-8'},
               {'content-type': 'application/xml;charset=utf-8'}
               ]


def post_http(data):

    action_data = json.dumps(data).encode('utf8')
    r = requests.post(session_http_url, data=action_data ,headers=headers[2])
    return r.json()

