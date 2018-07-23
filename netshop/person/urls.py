# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from person import views
from person.views import (CustomPersonDetailView, PersonUpdateView, PersonCreateView)

urlpatterns = [
  url(r'^person/$', views.person, name='person'),
  # url(r'^person/(?P<person_id>\d+)$', views.person_detail, name='person_detail'),
  url(r'^person/(?P<pk>\d+)$', CustomPersonDetailView.as_view(), name='person_detail'),
    url(r'^person/(?P<pk>\d+)/edit$', PersonUpdateView.as_view(), name='person_edit'),
    url(r'^add$', PersonCreateView.as_view(), name='person_add'),
]