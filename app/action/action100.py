#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/8 14:11
@Author  : fengweiqian
"""
from  app.action.action_base import ActionBase
from db.model.user import UserBase
from db.mysql_async import manager
from tool.time import timestamp2datetime,datetime2str

class Action100(ActionBase):
    """
    get one user base info
    """

    def __init__(self, request_data, ip):
        super(Action100, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=["courseId"])

    async def do_action(self):
        user_id = self.request_data.get('userId')
        u = await manager.get(UserBase, id=user_id)
        user = {"id": u.id,
                "name": u.name,
                "nickname": u.nickname,
                "phone": u.phone,
                "email": u.email,
                "itime": datetime2str(u.itime)}

        self.add_response('Data', user)


