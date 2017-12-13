#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description:
@Time    : 2017/12/12 16:33
@Author  : fengweiqian
"""
from db.models import UserBase
from db.mysql_manager import manager


async def get_user_base_info(user_id=None, phone=None, email=None):
    if user_id:
        u = await manager.get(UserBase, user_id=str(user_id))
    elif phone:
        u = await manager.get(UserBase, phone=phone)
    elif email:
        u = await manager.get(UserBase, email=email)
    else:
        return None
    return u


async def create_user(email=None, phone=None, password=None):

    await manager.create(UserBase, email=email, phone=phone, password=password)


