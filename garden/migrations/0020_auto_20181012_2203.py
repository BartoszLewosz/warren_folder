# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-12 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0019_auto_20181012_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.CharField(choices=[('1', 'EMERGENCY'), ('2', 'HIGH'), ('3', 'MEDIUM'), ('4', 'LOW')], default='', max_length=10),
        ),
    ]
