# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosmis_zh_cn', '0024_project_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_detail',
            name='download_url',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
