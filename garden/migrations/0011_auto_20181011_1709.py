# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-11 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden', '0010_auto_20181011_1627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='status',
            field=models.CharField(choices=[('!EMERGENCY', '!EMERGENCY'), ('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], default='', max_length=10),
        ),
    ]
