# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosmis_zh_cn', '0030_edu_book_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='edu',
            name='book_download',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
