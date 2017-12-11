#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description:
@Time    : 2017/12/11 17:02
@Author  : fengweiqian
"""
import peewee_async

database = peewee_async.MySQLDatabase('mooc',user="root", password="123456",host='fengweiqian.tech',port=3306)
manager = peewee_async.Manager(database)
database.set_allow_sync(False)