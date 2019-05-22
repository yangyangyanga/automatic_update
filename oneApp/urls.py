# -*- coding:utf-8 -*-
"""
# @PROJECT: automatic_update
# @Author: admin
# @Date:   2019-02-13 11:59:18
# @Last Modified by:   admin
# @Last Modified time: 2019-02-13 11:59:18
"""
from django.conf.urls import url
from django.urls import path

from . import views
app_name='oneApp'
urlpatterns = [
    path(r'', views.index, name='index'),   # 首页url
    path(r'england/', views.click_England, name='click_england'),
    path(r'australia/', views.click_Australia, name='click_australia'),
    path(r'canada/', views.click_Canada, name='click_canada'),

    path(r'showResult/<str:country>/<str:up>/', views.show_result, name='show_result'), # 传参数
    path(r'showtable/<str:country>/<int:pageid>/', views.get_monitor_copy1_data, name='get_monitor_copy1_data'),
    path(r'shishixinxi/<str:country>/', views.shishixinxi, name='shishixinxi')
]