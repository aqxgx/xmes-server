from rest_framework.routers import SimpleRouter
from mes.views import PartViewSet

app_name = 'mes'

router = SimpleRouter(False)
router.register('part', PartViewSet, basename='part')

urlpatterns = [
]
urlpatterns += router.urls