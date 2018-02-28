#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2018/02/28 11：34
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.course_component import get_created_courses
from app.componet.user_component import get_user_base_info


class Action202(ActionBase):
    """
    我创建的课程
    """

    def __init__(self, request_data, ip):
        super(Action202, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params()

    async def do_action(self):
        rtn_data = {}
        user_id = self.request_data.get('userId')
        user_base = await get_user_base_info(user_id=user_id)
        if not user_base.super_role:
            self.response_code = -101
            self.response_info = "account not teacher"
            return self.get_response()
        rtn_data["createdCourses"] = await get_created_courses(user_id)
        self.add_response('Data', rtn_data)