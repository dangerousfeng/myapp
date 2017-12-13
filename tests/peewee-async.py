#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/7 13:46
@Author  : fengweiqian
"""
from sanic import Sanic
import uvloop
from sanic.response import json
from signal import signal, SIGINT
import peewee
import asyncio
import peewee_async



app = Sanic(__name__)

async_db = peewee_async.MySQLDatabase('test',user="root", password="123456",host='fengweiqian.tech',port=3306)
db = peewee_async.Manager(database=async_db)
class AsyncHuman(peewee.Model):
    id = peewee.IntegerField()
    name = peewee.CharField()
    class Meta:
        database = async_db
        db_table = 'user'


@app.route('/session', methods=['GET', 'POST'])
async def session(request):
    obj = await db.create(
        AsyncHuman, name='12345')
    return json({'id': obj.id,
            'messenger_id': obj.name})

asyncio.set_event_loop(uvloop.new_event_loop())
server = app.create_server(host="0.0.0.0", port=5000)
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(server)
signal(SIGINT, lambda s, f: loop.stop())
try:
    loop.run_forever()
except:
    loop.stop()

