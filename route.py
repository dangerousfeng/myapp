#  -*- coding: utf-8 -*-
"""
Created on 2016.1.11

@author: DengShengjin
modify ChenJingYi 2017.3.7
"""
import json
import sys
import traceback

from app.action.action_base import lazy_import

if sys.version[0] == "2":
    from urllib import unquote
else:
    from urllib.parse import unquote

def get_params(request):
    """
    取出参数
    :return: ip, 参数
    """
    params = ''
    if request.method == 'GET':
        params = unquote(request.query_string).decode('utf8')
        params = json.loads(params)
    elif request.method == 'POST':
        params = request.json
    return params

async def exec_action(ip,request):
    try:
        # 获取参数
        params = get_params(request)
        action_id = params.get('ActionId', 0)
        # 反射实例化操作
        action_xxx = lazy_import(action_id)
        class_obj = action_xxx(params, ip)  # 类名为class_name的对象
        result = await class_obj.exec_action()  # 执行对象的exec_action方法d

    except Exception as e:
        traceback.print_exc()
        result = "exec_action exception"
    res = json.dumps(result).encode('utf8')
    return res
