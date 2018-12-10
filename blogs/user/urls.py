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
    url(r'^index/', views.index, name='index'),
    # 注销
    url(r'^logout/', views.logout, name='logout'),
    # 文章
    url(r'^article/', views.article, name='article'),
    # 添加文章
    url(r'^add_article/', views.add_article, name='add_article'),
    # 删除文章
    url(r'^del_article/(\d+)/', views.del_article, name='del_article'),
    # 更新数据
    url(r'^update_article/(\d+)/', views.update_article, name='update_article'),

    # 接受多个参数
    url(r'^args/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/', views.args, name='args'),


    # 测试上传图片
    url(r'^price/', views.price, name='price'),
    # 测试展示图片
    url(r'^show/', views.show, name='show'),

]
