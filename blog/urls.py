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

handler404 = 'views.page404'
handler500 = 'views.page500'

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<slug>[0-9a-zA-Z_\-]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchiveView.as_view(month_format='%m'),
        name='archives'),
    url(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tags'),
    url(r'^feed/$', AllPostsRssFeed(), name='rss'),
]
