# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosmis_zh_cn', '0020_auto_20170209_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
