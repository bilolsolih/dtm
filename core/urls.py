from django.contrib import admin
from django.urls import path, include

from .drf_schemas import swagger_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('banners/', include('apps.banners.urls', namespace='banners'))
]

urlpatterns += swagger_patterns
