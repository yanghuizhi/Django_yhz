# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Leo
# Time: 2020/4/13

"""
    利用另一种机制，实现当url过多时，将app分开
"""
# from boards import views
# from django.urls import path, re_path
#
#
# app_name = 'boards'
# urlpatterns = [
#     path('', views.home, name='home'),
#     re_path(r'boards/(?P<pk>\d+)/', views.board_topics, name='board_topics'),
# ]