#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2/26/18 4:44 AM
@Author  : fengweiqian
"""
from peewee import fn

from db.models import Course, Section, UserBase
from db.mysql_manager import manager
from tool.util import get_uuid


async def create_course(course_name, teacher_id, type, course_desc=None):
    course_id = get_uuid()
    course = await manager.create(Course,
                                  course_id=course_id,
                                  course_name=course_name,
                                  teacher_id=teacher_id,
                                  course_address=course_id + "/face",
                                  type=type,
                                  course_desc=course_desc)

    return course.course_id


async def create_section(course_id, sec_name, sec_desc=None):

    sq = Section.select().where(Section.course_id==course_id)
    sections = await manager.execute(sq)
    if sections:
        section_id = max([sec.section_id for sec in sections]) + 1
    else:
        section_id = 1
    # max_id = Section.select().aggregate(max('section_id')).where(course_id=course_id)
    section = await manager.create(Section,
                                   course_id=course_id,
                                   section_id=section_id,
                                   sec_name=sec_name,
                                   section_desc=sec_desc)

    return section.section_id


async def get_created_courses(user_id):

    course_list = []
    sq = Course.select().where(Course.teacher_id==user_id)
    courses = await manager.execute(sq)
    for c in courses:
        course_list.append(c.asDict())
    return course_list


async def get_course_detail(course_id):

    course = await manager.get(Course, course_id=course_id)
    teacher_id = course.teacher_id
    teacher = await manager.get(UserBase,user_id=teacher_id)
    teacher_name = teacher.user_name
    rtn_data = course.asDict()
    rtn_data["teacherName"] = teacher_name
    return rtn_data


async def get_sections_by_course(course_id):

    sq = Section.select().where(Section.course_id==course_id)
    secs = await manager.execute(sq)
    return [sec.asDict() for sec in secs]


async def get_top20_hot_courses():
    course_list = []
    sq = Course.select().order_by(Course.hot.desc()).limit(20)
    courses = await manager.execute(sq)
    for c in courses:
        course_list.append(c.asDict())
    return course_list


async  def get_recommend_4_courses():
    course_list = []
    sq = Course.select().order_by(fn.Rand()).limit(20)
    courses = await manager.execute(sq)
    for c in courses:
        course_list.append(c.asDict())
    return course_list