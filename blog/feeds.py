#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyCharm : 
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : feeds.py
@Created       : 2017/7/19
@Last Modified : 2017/7/19
"""
from django.contrib.syndication.views import Feed

from .models import Post


class AllPostsRssFeed(Feed):
    title = 'EINDEX\'s Blog'
    link = '/'
    description = "EINDEX 的博客"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '%s' % item.title

    def item_description(self, item):
        return item.body
