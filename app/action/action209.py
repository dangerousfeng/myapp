#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 3/14/18 7:20 AM
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.course_component import pull_collections_by_user


class Action209(ActionBase):
    """
    get collection course
    """

    def __init__(self, request_data, ip):
        super(Action209, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=[])

    async def do_action(self):
        rtn_data = {}
        user_id = self.request_data.get('userId')
        rtn_data["collectionCourses"] = await pull_collections_by_user(user_id=user_id)
        self.add_response('Data', rtn_data)

