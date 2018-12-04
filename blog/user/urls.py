# encoding: utf-8
"""
@author: 曹晓芹

"""
from django.conf.urls import url

from user import views

urlpatterns = [
    # 注册
    url(r'^register/', views.register, name='register'),
    # 登录
    url(r'^login/', views.login, name='login'),
    # 首页
    url(r'^index_back/', views.index_back, name='index_back'),
]
