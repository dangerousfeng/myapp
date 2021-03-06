#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
Module Description
@Time  : 2018/01/03 14：52
@Author: fengweiqian
"""


from aliyunsdkcore import client
from aliyunsdksts.request.v20150401 import AssumeRoleRequest
import json
import oss2
from itertools import islice



endpoint = 'oss-cn-beijing.aliyuncs.com'
bucket_name = 'mooc-feng'
# 子账号AccessKeyId
access_key_id = 'LTAIdCYLSKnUsb37'
# 子账号AccessKeySecret
access_key_secret = '65TpH3XXEdJSdHJuruQyZoaplqeK4q'
# 角色的资源描述符  只拥有只读权限的角色
role_arn = 'acs:ram::1363311981980278:role/moocfengappreadonly'
clt = client.AcsClient(access_key_id, access_key_secret, 'cn-beijing')
req = AssumeRoleRequest.AssumeRoleRequest()
# 为了简化讨论，这里没有设置Duration、Policy等，更多细节请参考RAM、STS的相关文档。
req.set_accept_format('json')  # 设置返回值格式为JSON
req.set_RoleArn(role_arn)
req.set_RoleSessionName('session-name')
req.set_DurationSeconds(1800)  # 半小时过期时间
body = clt.do_action_with_exception(req)
# 为了简化讨论，没有做出错检查
token = json.loads(body)


# ---------将token给客户端-----------------


# 初始化StsAuth实例
auth = oss2.StsAuth(token['Credentials']['AccessKeyId'],
                    token['Credentials']['AccessKeySecret'],
                    token['Credentials']['SecurityToken'])
# 初始化Bucket实例
bucket = oss2.Bucket(auth, endpoint, bucket_name)

# 列举Bucket里的10个文件
for b in islice(oss2.ObjectIterator(bucket), 10):
    print(b.key)

# 模拟文件夹 列举某个目录下所有文件
for obj in oss2.ObjectIterator(bucket, delimiter='/'):
    if obj.is_prefix():  # 文件夹
        print('directory: ' + obj.key)
    else:                # 文件
        print('file: ' + obj.key)