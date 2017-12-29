#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/29 14：33
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from config import OOS_PATH


class Action200(ActionBase):
    """
    create course
    """

    def __init__(self, request_data, ip):
        super(Action200, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=["courseName", "type"])

    async def do_action(self):
        teacher_id = self.request_data.get('userId')
        course_name = self.request_data.get('courseName')
        type = self.request_data.get('type')
        # course_address = OOS_PATH.join(["/",course_id])