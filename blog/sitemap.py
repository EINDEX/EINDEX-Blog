#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyCharm : 
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : sitemap.py
@Created       : 2017/7/23
@Last Modified : 2017/7/23
"""
from django.contrib.sitemaps import Sitemap

from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = 'daily'
    priority = .5

    def items(self):
        return Post.objects.filter(is_publish=True)

    def lastmod(self, post):
        return post.created_time
