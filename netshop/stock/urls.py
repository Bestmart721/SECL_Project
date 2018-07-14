# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from stock import views


urlpatterns = [
  url(r'^stock/$', views.stock, name='stock'),
  url(r'^stock/(?P<stock_id>\d+)$', views.stock_detail, name='stock_detail'),
]