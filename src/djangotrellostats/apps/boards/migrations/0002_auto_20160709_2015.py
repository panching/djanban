# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-09 18:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyspenttime',
            name='diff_time',
            field=models.DecimalField(decimal_places=4, default=None, max_digits=12, null=True, verbose_name='Difference between the estimated time and the spent time'),
        ),
        migrations.AddField(
            model_name='dailyspenttime',
            name='estimated_time',
            field=models.DecimalField(decimal_places=4, default=None, max_digits=12, null=True, verbose_name='Estimated time for this day'),
        ),
        migrations.AlterField(
            model_name='dailyspenttime',
            name='spent_time',
            field=models.DecimalField(decimal_places=4, default=None, max_digits=12, null=True, verbose_name='Spent time for this day'),
        ),
    ]