#!/usr/bin/env python
# -*- coding:utf-8 -*-
<<<<<<< HEAD
# project : xmes_server
=======
# project : xmes-server
>>>>>>> ff50a3cb99533137f0ba3053ad28c0b3f9ab2570
# filename : basic
# author : ly_13
# date : 7/31/2024

from common.utils import get_logger
from settings.serializers.basic import BasicSettingSerializer
from settings.views.settings import BaseSettingViewSet

logger = get_logger(__name__)


class BasicSettingViewSet(BaseSettingViewSet):
    """基本设置"""
    serializer_class = BasicSettingSerializer
    category = "basic"
