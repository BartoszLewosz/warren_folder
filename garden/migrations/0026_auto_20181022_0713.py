# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-22 07:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0025_auto_20181022_0711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.CharField(choices=[('EMERGENCY', '01_EMERGENCY'), ('HIGH', '02_HIGH'), ('MEDIUM', '03_MEDIUM'), ('LOW', '04_LOW')], default='', max_length=12),
        ),
    ]
