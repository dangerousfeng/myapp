#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/29 14：33
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.course_component import create_course
from app.componet.user_component import get_user_base_info
from tool.oss_sts import get_writeonly_sts_token

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
        course_desc = self.request_data.get('courseDesc',None)
        type = self.request_data.get('type')
        user_base = await get_user_base_info(user_id=teacher_id)
        if user_base.super_role != True:
            self.response_code = -101
            self.response_info = "account Lack of authority"
            return self.get_response()
        course_id = create_course(course_name,teacher_id,type,course_desc)
        # oos权限处理
        self.add_response('Data', {"courseId": course_id})
