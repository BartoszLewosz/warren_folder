# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-11 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0006_auto_20180611_1159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.CharField(default='', max_length=30),
        ),
    ]
