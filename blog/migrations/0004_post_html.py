# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-21 08:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_post_is_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='html',
            field=models.TextField(blank=True, editable=False),
        ),
    ]