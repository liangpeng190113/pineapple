# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 07:38
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodtopic',
            name='comments',
        ),
        migrations.AddField(
            model_name='foodtopic',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='多个标签以逗号分隔', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='标签'),
        ),
    ]
