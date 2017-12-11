#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/8 14:05
@Author  : fengweiqian
"""
import peewee
from server import mooc_db

class BaseModel(peewee.Model):
    """A base model that will use our MySQL database"""
    class Meta:
        database = mooc_db

class User(BaseModel):
    id = peewee.IntegerField()
    name = peewee.CharField()
    nickname = peewee.CharField()
    phone = peewee.IntegerField()
    email = peewee.CharField()
    password = peewee.CharField()
    itime = peewee.TimestampField()

