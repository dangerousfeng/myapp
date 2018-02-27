#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2017/12/8 14:05
@Author  : fengweiqian
"""
import peewee
from db.mysql_manager import database
import datetime
from tool.times import datetime2str
from tool.util import field_to_hump


class BaseModel(peewee.Model):
    """
    Base Model
    """
    def asDict(self):
        res = {}
        obj_dict = self.__dict__
        __data = obj_dict["_data"]
        for k, v in __data.items():
            value = v
            if isinstance(v, datetime.datetime):
                value = datetime2str(v)
            res[field_to_hump(k)]=value
        return res

    class Meta:
        database = database


class UserBase(BaseModel):
    """
    user base info
    """
    user_id = peewee.CharField(primary_key=True)
    user_name = peewee.CharField()
    phone = peewee.IntegerField()
    email = peewee.CharField()
    password = peewee.CharField()
    itime = peewee.DateTimeField()
    super_role = peewee.BooleanField()


class UserData(BaseModel):
    """
    user data
    """
    user_id = peewee.CharField(primary_key=True)
    nickname = peewee.CharField()
    money = peewee.IntegerField()


class Course(BaseModel):
    """
    course info
    """
    course_id = peewee.CharField(primary_key=True)
    course_name = peewee.CharField()
    teacher_id = peewee.CharField()
    hot = peewee.IntegerField()
    course_address = peewee.CharField()
    create_time = peewee.DateTimeField()
    type = peewee.IntegerField()
    course_desc = peewee.CharField()


class Section(BaseModel):
    """
    section info
    """
    course_id = peewee.CharField()
    section_id = peewee.IntegerField()
    sec_name = peewee.CharField()
    sec_desc = peewee.CharField()

    class Meta:
        primary_key = peewee.CompositeKey('course_id', 'section_id')
