# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20170218_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_date',
            field=models.CharField(default='', max_length=254),
        ),
    ]
