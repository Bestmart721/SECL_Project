# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from place import views


urlpatterns = [
  url(r'^place/$', views.place, name='place'),
  url(r'^place/(?P<place_id>\d+)$', views.place_detail, name='place_detail'),
]