# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-01-13 21:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dosmis_zh_cn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='learn',
            name='part_cn',
            field=models.CharField(default=datetime.datetime(2017, 1, 13, 21, 39, 8, 905426, tzinfo=utc), max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learn',
            name='part_describe_cn',
            field=models.CharField(default=datetime.datetime(2017, 1, 13, 21, 39, 18, 588449, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learn',
            name='part_describe_en',
            field=models.CharField(default=datetime.datetime(2017, 1, 13, 21, 39, 26, 955356, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learn',
            name='part_en',
            field=models.CharField(default=datetime.datetime(2017, 1, 13, 21, 39, 36, 381639, tzinfo=utc), max_length=45),
            preserve_default=False,
        ),
    ]
