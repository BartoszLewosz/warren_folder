# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-11 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0008_auto_20181011_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='author',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.CharField(choices=[('!_E_!', 'ASAP'), ('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], default='high', max_length=6),
        ),
    ]
