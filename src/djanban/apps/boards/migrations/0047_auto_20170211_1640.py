# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-11 15:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0046_auto_20170207_0108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='backward_movements',
        ),
        migrations.RemoveField(
            model_name='card',
            name='forward_movements',
        ),
        migrations.RemoveField(
            model_name='card',
            name='time',
        ),
    ]