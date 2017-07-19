#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyCharm : 
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : __init__.py.py
@Created       : 2017/7/19
@Last Modified : 2017/7/19
"""
import platform

if platform.node() == 'VM_9_200_centos':
    from .base import *
    from .server import *
else:
    from .base import *
    from .test import *
