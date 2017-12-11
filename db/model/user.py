#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/8 14:05
@Author  : fengweiqian
"""
import peewee
from db.mysql_async import database

class AsyncBaseModel(peewee.Model):
    class Meta:
        database = database


class User(AsyncBaseModel):
    id = peewee.IntegerField()
    name = peewee.CharField()
    nickname = peewee.CharField()
    phone = peewee.IntegerField()
    email = peewee.CharField()
    password = peewee.CharField()
    itime = peewee.TimestampField()

