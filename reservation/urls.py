"""reservation_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_type_id>\d+)/book', views.reserve, name='reserve'),
    url(r'^(?P<room_type_id>\d+)/detail', views.room_detail, name='room_detail'),
    url(r'^(?P<reservation_id>\d+)/remove', views.remove, name='remove'),
    url(r'^(?P<reservation_id>\d+)/checkin', views.checkin, name='checkin'),
    url(r'^(?P<reservation_id>\d+)/checkout', views.checkout, name='checkout')
]
