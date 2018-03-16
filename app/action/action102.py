#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/8 14:11
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.user_component import get_user_base_info,get_user_data_by_user_id
from db.mysql_manager import manager

class Action102(ActionBase):
    """
    change user base info
    """

    def __init__(self, request_data, ip):
        super(Action102, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=["userName", "phone", "email", "password", "nickName"])

    async def do_action(self):
        user_id = self.request_data.get('userId')

        user_base = await get_user_base_info(user_id=user_id)
        user_base.user_name = self.request_data.get('userName')
        user_base.phone = self.request_data.get('phone')
        user_base.email = self.request_data.get('email')
        user_base.password = self.request_data.get('password')
        await manager.update(user_base)

        nickname = self.request_data.get('nickName',None)
        if nickname:
            user_data = await get_user_data_by_user_id(user_id)
            user_data.nickname = nickname
            await manager.update(user_data)
        self.add_response('Data', {"success":1})