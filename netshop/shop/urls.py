# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.conf.urls import url
from shop import views
from shop.views import ShopCreateView, ShopUpdateView



urlpatterns = [
  url(r'^shop/$', views.shop, name='shop'),
  url(r'^shop/(?P<shop_id>\d+)$', views.shop_detail, name='shop_detail'),
  url(r'^shop/(?P<pk>\d+)/edit$', ShopUpdateView.as_view(), name='shop_edit'),
  url(r'^shop/add$', ShopCreateView.as_view(), name='shop_add'),

  # url(r'^shop/add$', CustomShopCreateView.as_view(), name='shop_add'),

]