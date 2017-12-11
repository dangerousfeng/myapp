#  -*- coding: utf-8 -*-
"""
Created on 2016.1.11

@author: DengShengjin
"""
import string
import time



IMPORT_ACTION ={}

def lazy_import(action_id):
    """
    write by Zhong Xianghua
    :param actionid:
    :return:
    """
    action_ids = str(action_id)
    key = action_ids
    if key in IMPORT_ACTION:
        return IMPORT_ACTION.get(key)
    module_name = 'app.action.action%s' % action_ids
    class_name = 'Action%s' % action_ids

    mod = __import__(module_name, None, None, [class_name])
    actcls = getattr(mod, class_name)
    IMPORT_ACTION[key] = actcls
    return actcls


class ActionBase(object):

    def __init__(self, request_data, ip):
        # 请求数据
        self.request_data = request_data
        # 请求的ip
        self.ip = ip
        # 请求接口id
        self.action_id = 0
        # 响应数据
        self.response_data = {}
        # 响应信息
        self.response_info = ''

    def verify_params(self):
        """
        验证参数
        :return:
        """
        return True

    def before_action(self):
        pass

    async def do_action(self):
        """
        业务逻辑处理函数
        :return:
        """
        pass

    def after_action(self):
        """
        do_action做完后调用
        :return:
        """
        pass

    async def exec_action(self):
        self.before_action()
        await self.do_action()
        self.after_action()
        return self.get_response()

    def get_response(self):
        """取得响应数据
        """
        if "Stat" not in self.response_data:
            self.add_response('Stat',0 )#self.response_code
        if "Info" not in self.response_data:
            self.add_response('Info', self.response_info)
        self.add_response('ActionId', self.action_id)
        return self.response_data

    def add_response(self, key, value):
        """添加响应数据
        :param key: 键
        :param value: 值
        """
        self.response_data[key] = value

    def add_response_dict(self, d):
        """添加响应数据
        :param d: dict格式的返回数据
        """
        self.response_data.update(d)
