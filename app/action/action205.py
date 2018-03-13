#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 3/11/18 6:08 AM
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.course_component import insert_one_comment


class Action205(ActionBase):
    """
    insert comment course
    """

    def __init__(self, request_data, ip):
        super(Action205, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=["courseId","content"])

    async def do_action(self):
        user_id = self.request_data.get('userId')
        course_id = self.request_data.get('courseId')
        content = self.request_data.get('content')

        comment = await insert_one_comment(course_id=course_id,user_id=user_id,content=content)
        return {"comment": comment}

