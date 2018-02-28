#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2018/02/28 13：53
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.course_component import get_sections_by_course


class Action203(ActionBase):
    """
    课程的所有小节
    """

    def __init__(self, request_data, ip):
        super(Action203, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=["courseId"])

    async def do_action(self):
        rtn_data = {}
        user_id = self.request_data.get('userId')
        course_id = self.request_data.get('courseId')
        rtn_data["sections"] = await get_sections_by_course(course_id=course_id)
        self.add_response('Data', rtn_data)