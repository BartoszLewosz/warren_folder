# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-12 22:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0020_auto_20181012_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.CharField(choices=[('EMERGENCY', '1'), ('HIGH', '2'), ('MEDIUM', '3'), ('LOW', '4')], default='', max_length=10),
        ),
    ]
