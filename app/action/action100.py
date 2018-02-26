#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/12 16：57
@Author  : fengweiqian
"""
from app.action.action_base import ActionBase
from app.componet.user_component import get_user_base_info, create_user, get_login_data


class Action100(ActionBase):
    """
    register user
    """

    def __init__(self, request_data, ip):
        super(Action100, self).__init__(request_data, ip)
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
        email = self.request_data.get('email')
        phone = self.request_data.get('phone')
        user = await get_user_base_info(email=email, phone=phone)
        if user:
            self.response_code = -100
            self.response_info = "user exist"
            return self.get_response()
        # create user
        password = self.request_data.get('password')
        super_role = self.request_data.get('superRole')
        user_base, user_data = await create_user(email=email, phone=phone, password=password, super_role=super_role)

        rtn_data = {"userBase": user_base.asDict(), "userData": user_data.asDict()}
        rtn_data.update(get_login_data(user_base, user_data))
        self.add_response('Data', rtn_data)