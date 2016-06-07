# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 08:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20160528_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='food.FoodCategory', verbose_name='分类'),
        ),
    ]