# encoding: utf-8
"""
@author: 曹晓芹

"""
from django.conf.urls import url

from web import views

urlpatterns = [
    url(r'^share/', views.share, name='share'),
    url(r'^list/', views.list, name='list'),
    url(r'^about/', views.about, name='about'),
    url(r'^gbook/', views.gbook, name='gbook'),
    url(r'^info/', views.info, name='info'),
    url(r'^index/', views.index, name='index'),
]
