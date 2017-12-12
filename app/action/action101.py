#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/8 14:11
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.user_component import get_user_base_info


class Action101(ActionBase):
    """
    user login
    """

    def __init__(self, request_data, ip):
        super(Action101, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=["courseId"])

    async def do_action(self):
        user_id = self.request_data.get('userId')
        user = await get_user_base_info(user_id=user_id)
        self.add_response('Data', user)


