#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 3/11/18 6:08 AM
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from db.model.user import UserBase
from db.mysql_async import manager
from tool.time import timestamp2datetime, datetime2str


class Action205(ActionBase):
    """
    comment course
    """

    def __init__(self, request_data, ip):
        super(Action205, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=["courseId"])

    async def do_action(self):
        user_id = self.request_data.get('userId')
        u = await manager.get(UserBase, id=user_id)
        self.add_response('Data', user)

