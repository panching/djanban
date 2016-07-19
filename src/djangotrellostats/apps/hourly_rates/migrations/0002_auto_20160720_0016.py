# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-19 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hourly_rates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hourlyrate',
            name='end_date',
            field=models.DateField(blank=True, default=None, help_text='End date of application of this billing rate', null=True, verbose_name='End date'),
        ),
    ]
