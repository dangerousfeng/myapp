#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description:
@Time    : 2017/12/12 16:33
@Author  : fengweiqian
"""
from db.mysql_async import manager
from tool.time import datetime2str
from db.model.user import UserBase


async def get_user_base_info(user_id=None, phone=None, email=None):
    if user_id:
        u = await manager.get(UserBase, id=user_id)
    elif phone:
        u = await manager.get(UserBase, phone=phone)
    elif email:
        u = await manager.get(UserBase, email=email)
    else:
        return None
    user = {"id": u.id,
            "name": u.name,
            "nickname": u.nickname,
            "phone": u.phone,
            "email": u.email,
            "itime": datetime2str(u.itime)}
    return user


async def create_user(email=None, phone=None, password=None):

    await manager.create(UserBase, email=email, phone=phone, password=password)


