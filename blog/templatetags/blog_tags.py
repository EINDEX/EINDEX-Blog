#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
PyCharm : 
Copyright (C) 2016-2017 EINDEX Li

@Author        : EINDEX Li
@File          : blog_tags.py
@Created       : 2017/7/15
@Last Modified : 2017/7/15
"""
from django import template
from django.db.models import Count

from ..models import Post, Tag

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time').filter(is_publish=True)[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC').filter(is_publish=True)


@register.simple_tag
def get_tags():
    # todo 标签云显示未发布文章
    post_list = Post.objects.filter(is_publish=True)
    return Tag.objects.annotate(num_posts=Count(post_list)).filter(num_posts__gt=0)
