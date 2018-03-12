#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2018/03/06 11：27
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.course_component import get_sections_by_course, get_course_detail, pull_course_comments
from app.componet.user_component import get_user_data_by_user_id, get_user_base_info, get_user_name


class Action204(ActionBase):
    """
    课程详情页（基本资料，小节，评论）
    """

    def __init__(self, request_data, ip):
        super(Action204, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def before_action(self):
        return self.check_params(params=["courseId"])

    async def do_action(self):
        rtn_data = {}
        user_id = self.request_data.get('userId')
        course_id = self.request_data.get('courseId')
        rtn_data["course"] = await get_course_detail(course_id)
        rtn_data["sections"] = await get_sections_by_course(course_id=course_id)

        comment_list = []
        comments = await pull_course_comments(course_id=course_id)
        for comm in comments:
            u_name = await get_user_name(user_id=comm.user_id)
            item_data = comm.asDict()
            item_data.update({"uName":u_name})
            comment_list.append(item_data)
        rtn_data["comments"] = comment_list

        self.add_response('Data', rtn_data)