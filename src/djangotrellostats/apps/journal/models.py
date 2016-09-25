# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


# Each one of the journal entries
class JournalEntry(models.Model):

    board = models.ForeignKey("boards.Board", verbose_name=u"Board", related_name="journal_entries")

    author = models.ForeignKey("members.Member", verbose_name=u"Member", related_name="journal_entries")

    title = models.CharField(verbose_name=u"Title", max_length=128)

    slug = models.SlugField(verbose_name=u"Slug for this journal entry", max_length=64, unique=True)

    uuid = models.CharField(verbose_name=u"Unique uuid for short urls", max_length=16, unique=True)

    content = models.TextField(verbose_name=u"Content", help_text=u"Content of this journal entry")

    creation_datetime = models.DateTimeField(verbose_name=u"Creation datetime")

    last_update_datetime = models.DateTimeField(verbose_name=u"Last update datetime")
