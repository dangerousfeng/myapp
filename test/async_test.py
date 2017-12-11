#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/11 16:56
@Author  : fengweiqian
"""
import asyncio
import peewee
import peewee_async

database = peewee_async.MySQLDatabase('mooc',user="root", password="123456",host='fengweiqian.tech',port=3306)

class User(peewee.Model):
    id = peewee.IntegerField()
    name = peewee.CharField()
    nickname = peewee.CharField()
    phone = peewee.IntegerField()
    email = peewee.CharField()
    password = peewee.CharField()
    itime = peewee.TimestampField()
    class Meta:
        database = database

objects = peewee_async.Manager(database)

database.set_allow_sync(False)

async def handler():
    all_objects = await objects.execute(User.select())
    for obj in all_objects:
        print("user_id:",obj.id)
        print("user_name:",obj.name)

loop = asyncio.get_event_loop()
loop.run_until_complete(handler())
loop.close()