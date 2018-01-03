#!/usr/bin/env python
# -*- coding:utf-8 -*- 
"""
Module Description
@Time  : 2018/01/03 10：28
@Author: fengweiqian
"""
import oss2
from itertools import islice

auth = oss2.Auth('LTAI7G26axcT3paO', 'FrIXPACnbwcqWLI9vMynwlqWmJFnsU')
endpoint = 'oss-cn-beijing.aliyuncs.com'
bucket = oss2.Bucket(auth, endpoint, 'mooc-feng', connect_timeout=30)
service = oss2.Service(auth, endpoint)

# 查看bucket权限
print("bucket权限", bucket.get_bucket_acl().acl)

# oss2.Service是用来访问“OSS服务”相关的类，目前只是用来列举用户的Bucket
print([b.name for b in oss2.BucketIterator(service)])

# 列举Bucket里的10个文件
for b in islice(oss2.ObjectIterator(bucket), 10):
    print(b.key)

# 模拟文件夹 列举某个目录下所有文件
for obj in oss2.ObjectIterator(bucket, delimiter='/'):
    if obj.is_prefix():  # 文件夹
        print('directory: ' + obj.key)
    else:                # 文件
        print('file: ' + obj.key)