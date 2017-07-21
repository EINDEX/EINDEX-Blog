#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyCharm : 
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : urls.py
@Created       : 2017/7/15
@Last Modified : 2017/7/15
"""
from django.conf.urls import url

from . import views

app_name = 'comments'
urlpatterns = [
    # url(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment')
]