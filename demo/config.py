#!/usr/bin/env python
# -*- coding:utf-8 -*-
<<<<<<< HEAD
# project : xmes_server
=======
# project : xmes-server
>>>>>>> ff50a3cb99533137f0ba3053ad28c0b3f9ab2570
# filename : config
# author : ly_13
# date : 6/12/2024


from django.urls import path, include

# 路由配置，当添加APP完成时候，会自动注入路由到总服务
URLPATTERNS = [
    path('api/demo/', include('demo.urls')),
]
# 请求白名单，支持正则表达式，可参考settings.py里面的 PERMISSION_WHITE_URL
PERMISSION_WHITE_REURL = []
