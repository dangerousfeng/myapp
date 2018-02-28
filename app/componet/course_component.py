#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 2/26/18 4:44 AM
@Author  : fengweiqian
"""

from db.models import Course, Section
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

    sq = Section.select().where(course_id=course_id)
    sections = await sq.excute()
    section_id = max([Section.section_id for Section.section_id in sections]) + 1
    # max_id = Section.select().aggregate(max('section_id')).where(course_id=course_id)
    section = await manager.create(Section,
                                   course_id=course_id,
                                   section_id=section_id,
                                   sec_name=sec_name,
                                   sec_desc=sec_desc)

    return section.section_id


async def get_created_courses(user_id):

    course_list = []
    sq = Course.select().where(teacher_id=user_id)
    courses = await sq.excute()
    for c in courses:
        course_list.append(c.asDict())
    return course_list


async def get_sections_by_course(course_id):

    sq = Section.select().where(course_id=course_id)
    secs = await sq.excute()
    return [sec.asDict for sec in secs]
