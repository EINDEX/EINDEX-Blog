# Generated by Django 2.0.dev20170801131532 on 2017-08-01 13:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0008_auto_20170801_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='absolute_url',
            field=models.SlugField(unique=True),
        ),
    ]
