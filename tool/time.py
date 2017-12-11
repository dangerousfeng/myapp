#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module Description: 
@Time    : 12/11/17 5:13 AM
@Author  : fengweiqian
"""
import time,datetime
from datetime import datetime

def datetime2str(datetime):
    return datetime.strftime("%Y-%m-%d %H:%M:%S")

def timestamp2datetime(timestamp):
    return datetime.fromtimestamp(timestamp)

def datetime2timestamp(datetime):
    return  time.mktime(datetime.timetuple())


if __name__=='__main__':
    times = time.time()
    print(times)
    dt = timestamp2datetime(times)
    print(dt)
    print(datetime2str(dt))