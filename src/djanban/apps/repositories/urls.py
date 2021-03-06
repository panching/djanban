# -*- coding: utf-8 -*-

from django.conf.urls import url, include

from djanban.apps.repositories.views.repositories import view_list, new, view, edit, delete, checkout
from djanban.apps.repositories.views.commits import add as add_commit, delete as delete_commit, \
    view_assessment_report

urlpatterns = [

    # List of repositories of this project
    url(r'^$', view_list, name="view_repositories"),

    url(r'^(?P<type>gitlab)/new/?$', new, name="new_repository"),
    url(r'^(?P<type>github)/new/?$', new, name="new_repository"),

    url(r'^(?P<repository_id>\d+)/view/?$', view, name="view_repository"),

    url(r'^(?P<repository_id>\d+)/checkout/?$', checkout, name="checkout_repository"),

    url(r'^(?P<repository_id>\d+)/commits/add/?$', add_commit, name="add_commit"),

    url(r'^(?P<repository_id>\d+)/commits/(?P<commit_id>\d+)/view_assessment_report/?$', view_assessment_report, name="view_assessment_report"),

    url(r'^(?P<repository_id>\d+)/commits/(?P<commit_id>\d+)/delete/?$', delete_commit, name="delete_commit"),

    url(r'^(?P<repository_id>\d+)/edit/?$', edit, name="edit_repository"),

    url(r'^(?P<repository_id>\d+)/delete/?$', delete, name="delete_repository"),
]
