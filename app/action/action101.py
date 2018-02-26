#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/8 14:11
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.user_component import get_user_base_info, get_user_data_by_user_id, get_login_data


class Action101(ActionBase):
    """
    user login
    """

    def __init__(self, request_data, ip):
        super(Action101, self).__init__(request_data, ip)
        self.action_id = int(self.__class__.__name__.replace('Action', ''))

    def check_params(self, params=[]):
        """
        check参数
        :return:
        """
        params = ["email", "phone", ]
        for param in params:
            value = self.request_data.get(param, None)
            if value and self.request_data.get("password"):
                return True
        self.response_code = -2
        self.response_info = "params error"
        return False

    def before_action(self):
        return self.check_params()

    async def do_action(self):
        # check phone or email exist
        email = self.request_data.get('email',None)
        phone = self.request_data.get('phone',None)
        user_base = await get_user_base_info(email=email, phone=phone)
        if not user_base:
            self.response_code = -100
            self.response_info = "account not exist"
            return self.get_response()
        if user_base.password != self.request_data.get("password"):
            self.response_code = -100
            self.response_info = "password error"
            return self.get_response()
        user_data = await get_user_data_by_user_id(user_base.user_id)

        # todo get login data, init data
        rtn_data = {"userBase": user_base.asDict(), "userData": user_data.asDict()}
        rtn_data.update(get_login_data(user_base,user_data))
        self.add_response('Data', rtn_data)