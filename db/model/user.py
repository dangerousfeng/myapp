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
    """
    Base Model
    """
    def get_dict(self):
        pass

    class Meta:
        database = database


class UserBase(AsyncBaseModel):
    """
    user base info
    """
    user_id = peewee.CharField()
    user_name = peewee.CharField()
    phone = peewee.IntegerField()
    email = peewee.CharField()
    password = peewee.CharField()
    itime = peewee.TimestampField()


class UserData(AsyncBaseModel):
    """
    user data
    """
    user_id = peewee.CharField()
    nickname = peewee.CharField()
    money = peewee.IntegerField()


class Course(AsyncBaseModel):
    """
    course info
    """
    course_id = peewee.IntegerField()
    course_name = peewee.CharField()
    teacher_id = peewee.CharField()
    hot = peewee.IntegerField()
    course_address = peewee.CharField()


class Section(AsyncBaseModel):
    """
    section info
    """
    course_id = peewee.IntegerField()
    section_id = peewee.IntegerField()
    sec_name = peewee.CharField()