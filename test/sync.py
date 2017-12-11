#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author: WeiQian Feng


import peewee
from peewee import MySQLDatabase,Model

mysql_db = MySQLDatabase("mooc", user="root", passwd="123456",host='fengweiqian.tech',port=3306)

mysql_db.connect()  # 连接数据库

class MySQLModel(Model):
    class Meta:
        database = mysql_db

class User(MySQLModel): #类的小写即表名
    id = peewee.IntegerField() #字段声明
    name = peewee.CharField()
    nickname = peewee.CharField()
    phone = peewee.IntegerField()
    email = peewee.CharField()
    password = peewee.CharField()
    itime = peewee.TimestampField()

users = User.select()
for u in users:
    print(u.id,u.name,u.nickname,u.phone,u.email,u.phone,u.itime)

