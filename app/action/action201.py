#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2/26/18 6:23 AM
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.course_component import create_section


class Action201(ActionBase):
    """
    create section
    """

    def __init__(self, request_data, ip):
        super(Action201, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=["courseId","secName"])

    async def do_action(self):
        course_id = self.request_data.get('courseId')
        sec_name = self.request_data.get('secName')
        sec_desc = self.request_data.get('secDesc',None)
        sec_id = await create_section(course_id,sec_name,sec_desc)
        self.add_response('Data', {'secId':sec_id})

