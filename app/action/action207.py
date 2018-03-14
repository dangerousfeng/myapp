#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2018/03/14 15：47
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.course_component import zan_add


class Action207(ActionBase):
    """
    对评论点赞
    """

    def __init__(self, request_data, ip):
        super(Action207, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=["commentId"])

    async def do_action(self):
        user_id = self.request_data.get('userId')
        comment_id = self.request_data.get('commentId')
        await zan_add(comment_id=comment_id)
        self.add_response('Data', {"success":1})
