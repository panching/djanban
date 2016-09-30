# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

from djangotrellostats.apps.index import views as index_views

urlpatterns = [
    url(r'^$', index_views.index, name="index"),

    url(r'^admin/', admin.site.urls),

    url(r'^base/', include('djangotrellostats.apps.base.urls', namespace="base")),
    url(r'^member/', include('djangotrellostats.apps.members.urls', namespace="members")),
    url(r'^boards/', include('djangotrellostats.apps.boards.urls', namespace="boards")),
    url(r'^times/', include('djangotrellostats.apps.dev_times.urls', namespace="dev_times")),
    url(r'^charts/', include('djangotrellostats.apps.charts.urls', namespace="charts")),
    url(r'^hourly_rates/', include('djangotrellostats.apps.hourly_rates.urls', namespace="hourly_rates")),
    url(r'^fetch/', include('djangotrellostats.apps.fetch.urls', namespace="fetch")),
    url(r'^environment/', include('djangotrellostats.apps.dev_environment.urls', namespace="dev_environment")),
    url(r'^slideshow/', include('djangotrellostats.apps.slideshow.urls', namespace="slideshow")),
    url(r'^visitors/', include('djangotrellostats.apps.visitors.urls', namespace="visitors")),
    url(r'^niko-niko-calendar/', include('djangotrellostats.apps.niko_niko_calendar.urls', namespace="niko_niko_calendar")),

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
