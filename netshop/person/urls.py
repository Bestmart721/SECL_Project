# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from person import views

urlpatterns = [
  url(r'^person/$', views.person, name='person'),
  url(r'^person/(?P<person_id>\d+)$', views.person_detail, name='person_detail'),
]