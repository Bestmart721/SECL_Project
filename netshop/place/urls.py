# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from place import views
from place.models import City, Country
from django.views.generic import UpdateView, CreateView, ListView, DetailView


urlpatterns = [
  url(r'^place/$', views.place, name='place'),
  url(r'^place/(?P<place_id>\d+)$', views.place_detail, name='place_detail'),
  url(r'^country/list$', ListView.as_view(model=Country), name='country_list'),
  url(r'^country/(?P<pk>\d+)$', DetailView.as_view(model=Country), name='country_detail'),

  url(r'^place/(?P<pk>\d+)/edit$', UpdateView.as_view(model=City, fields=('name', 'country')),
      name='place_edit'),
  url(r'^place/add$', CreateView.as_view(model=City, fields=('name', 'country')), name='place_add'),
  url(r'^country/(?P<pk>\d+)/edit$', UpdateView.as_view(model=Country, fields=('name',)),
      name='country_edit'),
    url(r'^country/add$', CreateView.as_view(model=Country, fields=('name',)), name='country_add')
]