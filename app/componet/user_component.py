#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description:
@Time    : 2017/12/12 16:33
@Author  : fengweiqian
"""
from db.models import UserBase
from db.mysql_manager import manager
from tool.util import get_uuid


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


async def create_user(email=None, phone=None, password=None, super_role=False):
    user_id = get_uuid()
    name = email if email else phone
    user_base = await manager.create(UserBase, user_id=user_id, name=name, email=email, phone=phone,  password=password, super_role=super_role)


# if __name__=="__main__":
