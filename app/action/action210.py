#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 3/14/18 7:25 AM
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.course_component import pull_play_records_by_user


class Action210(ActionBase):
    """
    pull play record
    """

    def __init__(self, request_data, ip):
        super(Action210, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=[])

    async def do_action(self):
        rtn_data = {}
        user_id = self.request_data.get('userId')
        rtn_data["playRecords"] = await pull_play_records_by_user(user_id=user_id)
        self.add_response('Data', rtn_data)

