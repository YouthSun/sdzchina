# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dosmis_zh_cn', '0005_edu_book_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.IntegerField(default=0)),
                ('daytime', models.CharField(max_length=2, null=True)),
            ],
        ),
    ]
