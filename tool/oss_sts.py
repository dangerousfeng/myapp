#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
Module Description
@Time  : 2018/01/04 14：07
@Author: fengweiqian
"""
from aliyunsdkcore import client
from aliyunsdksts.request.v20150401 import AssumeRoleRequest
import json
import oss2
from itertools import islice
from config import *


def get_sts_token(role_arn):
    """
    通过role_arn获取token
    :param role_arn:
    :return:
    """
    # endpoint = OSS_ENDPOINT
    # bucket_name = OSS_BUCKET_NAME
    # 子账号AccessKeyId
    access_key_id = OSS_ACCESS_KEY_ID
    # 子账号AccessKeySecret
    access_key_secret = OSS_ACCESS_KEY_SECRET
    clt = client.AcsClient(access_key_id, access_key_secret, OSS_REGION_ID)
    req = AssumeRoleRequest.AssumeRoleRequest()
    # 为了简化讨论，这里没有设置Duration、Policy等，更多细节请参考RAM、STS的相关文档。
    req.set_accept_format('json')  # 设置返回值格式为JSON
    req.set_RoleArn(role_arn)
    req.set_RoleSessionName('session-name')
    req.set_DurationSeconds(1800)  # 半小时过期时间
    body = clt.do_action_with_exception(req)
    # 为了简化讨论，没有做出错检查
    token = json.loads(body)
    return token['Credentials']


def get_readonly_sts_token():
    """
    获取只读权限
    :return:
    """
    return get_sts_token(READ_ONLY_ROLE_ARN)


def get_writeonly_sts_token():
    """
    获取只写权限
    :return:
    """
    return get_sts_token(WRITE_ONLY_ROLE_ARN)
