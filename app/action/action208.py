#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2018/03/14 15：55
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.course_component import get_courses_by_type


class Action208(ActionBase):
    """
    获取分类课程
    """

    def __init__(self, request_data, ip):
        super(Action208, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=["type"])

    async def do_action(self):
        user_id = self.request_data.get('userId')
        c_type = self.request_data.get('type')
        courses = await get_courses_by_type(c_type=c_type)
        self.add_response('Data', {"typeCourses":courses})
