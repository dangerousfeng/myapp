#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description:
@Time    : 2017/12/12 16:33
@Author  : fengweiqian
"""
from db.models import UserBase, UserData
from db.mysql_manager import manager
from tool.oss_sts import get_writeonly_sts_token, get_readonly_sts_token
from tool.util import get_uuid


async def get_login_data(user_base,user_data):

    rtn_data = {}

    rtn_data["stsReadOnly"] = await get_readonly_sts_token()
    if user_base.super_role == True:
        rtn_data["stsWriteOnly"] = await get_writeonly_sts_token()

    rtn_data["JWT"] = "THIS IS A JWT."
    return rtn_data


async def get_user_base_info(user_id=None, phone=None, email=None):
    try:
        if user_id:
            u = await manager.get(UserBase, user_id=str(user_id))
        elif phone:
            u = await manager.get(UserBase, phone=phone)
        elif email:
            u = await manager.get(UserBase, email=email)
        else:
            return None
    except UserBase.DoesNotExist:
        u = None
    return u


async def get_user_data_by_user_id(user_id):
    try:
        user_data = await manager.get(UserData, user_id=str(user_id))
    except UserData.DoesNotExist:
        user_data = None
    return user_data


async def create_user(email=None, phone=None, password=None, super_role=False):
    user_id = get_uuid()
    nickname = email if email else phone
    user_base = await manager.create(UserBase, user_id=user_id, email=email, phone=phone,  password=password, super_role=super_role)
    user_data = await manager.create(UserData, user_id=user_id, nickname=nickname,money=100000)
    # todo new user init
    return user_base, user_data

# if __name__=="__main__":
