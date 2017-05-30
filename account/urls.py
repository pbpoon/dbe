# _*_ conding:utf-8 _*_
__author__ = 'pbpoon'
__date__ = '2017/5/30 21:43'

from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    url(r'^edit/$', views.EditView.as_view(), name='edit'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^logout/$', auth_view.logout, name='logout'),
    url(r'^login/$', auth_view.login, name='login'),
    url(r'^$', views.DashboardView.as_view(), name='dashboard'),
    # change password urls
    url(r'^password-change/$',
        auth_view.password_change,
        name='password_change'),
    url(r'^password-change/done/$',
        auth_view.password_change_done,
        name='password_change_done'),

    # restore password urls
    url(r'^password-reset/$',
        auth_view.password_reset,
        name='password_reset'),
    url(r'^password-reset/done/$',
        auth_view.password_reset_done,
        name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_view.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^password-reset/complete/$',
        auth_view.password_reset_complete,
        name='password_reset_complete'),
]
