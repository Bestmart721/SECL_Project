# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from shop import views


urlpatterns = [
  url(r'^shop/$', views.shop, name='shop'),
  url(r'^shop/(?P<shop_id>\d+)$', views.shop_detail, name='shop_detail'),
]