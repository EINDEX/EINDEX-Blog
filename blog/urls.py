#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyCharm : 
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : url.py
@Created       : 2017/7/15
@Last Modified : 2017/7/15
"""
from django.conf.urls import url

from blog.feeds import AllPostsRssFeed
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tags'),
    url(r'^feed/$', AllPostsRssFeed(), name='rss')
]
