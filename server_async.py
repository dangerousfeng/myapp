#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/11 17:02
@Author  : fengweiqian
"""
import asyncio
from signal import signal, SIGINT
import traceback
import uvloop
from sanic import Sanic
from sanic import response
# from mooc.tool import server_config

app = Sanic(__name__)
# app.config.from_object(server_config)

def get_IP(request):
    if request.headers.get('X-Forwarded-For'):
        ip = request.headers.get('X-Forwarded-For').split(',')[-1]
    else:
        ip = request.ip if request.ip else ''
    return ip

@app.route('/mooc', methods=['POST'])
async def session(request):
    from route import exec_action
    try:
        ip = get_IP(request)
        resp = await exec_action(ip, request)
        return response.json(resp)
    except:
        traceback.print_exc()
        return "hahaha"

asyncio.set_event_loop(uvloop.new_event_loop())
server = app.create_server(host="0.0.0.0", port=5000)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(server)
signal(SIGINT, lambda s, f: loop.stop())

try:
    loop.run_forever()
except:
    loop.stop()
