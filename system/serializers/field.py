#!/usr/bin/env python
# -*- coding:utf-8 -*-
<<<<<<< HEAD
# project : xmes_server
=======
# project : xmes-server
>>>>>>> ff50a3cb99533137f0ba3053ad28c0b3f9ab2570
# filename : field
# author : ly_13
# date : 8/10/2024

from common.core.serializers import BaseModelSerializer
from common.utils import get_logger
from system.models import ModelLabelField

logger = get_logger(__name__)


class ModelLabelFieldSerializer(BaseModelSerializer):
    class Meta:
        model = ModelLabelField
        fields = ['pk', 'name', 'label', 'parent', 'field_type', 'created_time', 'updated_time']
        read_only_fields = [x.name for x in ModelLabelField._meta.fields]
        extra_kwargs = {'parent': {'attrs': ['pk', 'name', 'label'], 'read_only': True, 'format': '{label}({pk})'}}


class ModelLabelFieldImportSerializer(BaseModelSerializer):
    class Meta:
        model = ModelLabelField
        fields = ['pk', 'name', 'label', 'parent', 'field_type', 'created_time', 'updated_time']
