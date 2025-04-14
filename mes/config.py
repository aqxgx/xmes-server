from django.urls import path, include

URLPATTERNS = [
    path('api/mes/', include('mes.urls')),
]

PERMISSION_WHITE_REURL = []