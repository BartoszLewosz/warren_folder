# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-11-16 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0003_auto_20181022_0809'),
    ]

    operations = [
        migrations.AddField(
            model_name='maintenance',
            name='priority',
            field=models.CharField(choices=[('EMERGENCY', 'EMERGENCY'), ('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], default='EMERGENCY', max_length=30),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='status',
            field=models.CharField(choices=[('IN_PROGRESS', 'IN PROGRESS'), ('QUEUE', 'QUEUE'), ('CANCELED', 'CANCELED'), ('COMPLETED', 'COMPLETED')], default='QUEUE', max_length=30),
        ),
    ]