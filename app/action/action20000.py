#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/8 14:11
@Author  : fengweiqian
"""
from  app.action.action_base import ActionBase
from db.model.user import User
from server_async import objects

import traceback

class Action20000(ActionBase):
    """
    增加一个共享秘钥、客户端密钥到会话管理
    """

    def __init__(self, request_data, ip):
        super(Action20000, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))
        self.JWT = ''
        self.Key = ''
        self.c_pub = ''

    def verify_params(self):
        self.JWT = self.request_data.get('JWT', '')
        self.Key = self.request_data.get('Key', '')
        self.c_pub = self.request_data.get('c_pub', '')
        if self.JWT and self.Key and self.c_pub:
            return True
        return False

    async def do_action(self):
        user_list = []
        # users = User.select()
        users = await objects.execute(User.select())
        for u in users:
            item = {"id":u.id,"name":u.name, "nickname":u.nickname,"phone":u.phone, "email":u.email}
            print(item)
            user_list.append(item)
        self.add_response('Data',user_list)


