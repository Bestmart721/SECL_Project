# coding=utf-8


"""netshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from netshop import views

urlpatterns = [
    url(r'^main/(?P<i>\d+)/(?P<j>\d+)/$', views.main),#http://127.0.0.1:8000/main/1/2/
    url(r'^main/(?P<i>\d+)/default/$', views.main),#http://127.0.0.1:8000/main/1/default/ приклад силок ?P<i> i цце щмынна з вюхи
    url(r'^main/(?P<i>\d+)/special/$', views.main, kwargs={'j': -1}),#http://127.0.0.1:8000/main/1/special/ передасть -1
    url(r'^admin/', admin.site.urls),

    url(r'^post/(?P<slug>[\w\-]+)', views.post, name='news_post'),#reverse('news_post', kwargs={'slug': 'hello-world'}) приклад для чоого потрыбен нейм

]
