# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from stock import views
from stock.views import (StockUpdateView, StockCreateView)
from django.views.generic import DeleteView, UpdateView, CreateView



urlpatterns = [
  url(r'^stock/$', views.stock, name='stock'),
  url(r'^stock/(?P<pk>\d+)$', views.stock_detail, name='stock_detail'),
  url(r'^stock/(?P<pk>\d+)/edit$', StockUpdateView.as_view(), name='stock_edit'),
  url(r'^stock/add$', StockCreateView.as_view(), name='stock_add'),

]