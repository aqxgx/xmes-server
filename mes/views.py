from django_filters import rest_framework as filters
from rest_framework.decorators import action

from common.core.filter import BaseFilterSet
from common.core.modelset import BaseModelSet, ImportExportDataAction
from common.core.pagination import DynamicPageNumber
from common.core.response import ApiResponse
from common.utils import get_logger
from mes.models import Part
from mes.utils.serializer import PartSerializer

logger = get_logger(__name__)

class PartViewSetFilter(BaseFilterSet):
    part_number = filters.CharFilter(field_name='part_number', lookup_expr='icontains')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Part
        fields = ['part_number', 'name', 'unit', 'price']

class PartViewSet(BaseModelSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    ordering_fields = ['name', 'price']
    filterset_class = PartViewSetFilter

    @action(methods=['post'], detail=True)
    def push(self, request, *args, **kwargs):
        instance = self.get_object()
        return ApiResponse(detail=f"{instance.name} 推送成功")
