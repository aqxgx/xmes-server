from rest_framework import serializers
from common.core.serializers import BaseModelSerializer
from common.fields.utils import input_wrapper
from mes import models

class PartSerializer(BaseModelSerializer):
    class Meta:
        model = models.Part
        fields = [
            'pk', 'part_number', 'name', 'unit', 'drawing_number', 'spec1', 'spec2', 'spec3', 'spec4', 'spec5', 'spec6', 'spec7', 'spec8', 'spec9', 'price'
        ]
        table_fields = [
            'pk', 'part_number', 'name', 'unit', 'drawing_number', 'price'
        ]
        extra_fields = [
            'spec1', 'spec2', 'spec3', 'spec4', 'spec5', 'spec6', 'spec7', 'spec8', 'spec9'
        ]
        read_only_fields = ['pk']
    # block = input_wrapper(serializers.SerializerMethodField)(read_only=True, input_type='boolean',
    #                                                             label="自定义input_type")

    # def get_block(self, obj):
    #     return obj.is_active