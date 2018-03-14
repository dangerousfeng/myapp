#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2018/03/14 15：32
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.course_component import insert_one_collection


class Action206(ActionBase):
    """
    insert collection course
    """

    def __init__(self, request_data, ip):
        super(Action206, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=["courseId"])

    async def do_action(self):
        user_id = self.request_data.get('userId')
        course_id = self.request_data.get('courseId')
        collection = await insert_one_collection(user_id=user_id,course_id=course_id)
        self.add_response('Data', {"collection":collection.asDict()})
