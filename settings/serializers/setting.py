#!/usr/bin/env python
# -*- coding:utf-8 -*-
<<<<<<< HEAD
# project : xmes_server
=======
# project : xmes-server
>>>>>>> ff50a3cb99533137f0ba3053ad28c0b3f9ab2570
# filename : settings
# author : ly_13
# date : 10/25/2024
from common.core.serializers import BaseModelSerializer
from settings.models import Setting


class SettingSerializer(BaseModelSerializer):
    class Meta:
        model = Setting
        fields = ['pk', 'name', 'value', 'category', 'is_active', 'encrypted', 'created_time']
        read_only_fields = ['pk']
