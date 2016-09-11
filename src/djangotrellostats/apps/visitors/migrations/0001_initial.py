# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-11 14:02
from __future__ import unicode_literals

from django.contrib.auth.models import Group
from django.db import migrations


def create_visitors_group(apps, schema):
    if not Group.objects.filter(name=u"Visitors").exists():
        visitors_group = Group(name=u"Visitors")
        visitors_group.save()


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(create_visitors_group)
    ]
