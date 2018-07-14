# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from netshop import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^admin/', admin.site.urls),

    url(r'^', include('person.urls')),
    url(r'^', include('place.urls')),
    url(r'^', include('shop.urls')),
    url(r'^', include('stock.urls')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_URL)

