# _*_ coding:utf-8 _*_
__author__ = 'pb'
__date__ = '2017/5/31 10:09'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^image/$', views.ImageListView.as_view(), name='list'),
    url(r'^image/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create/$', views.ImageCreateView.as_view(), name='create'),
]
