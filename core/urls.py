from django.contrib import admin
from django.urls import path, include

from .drf_schemas import swagger_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('banners/', include('apps.banners.urls', namespace='banners')),
    path('tests/', include('apps.tests.urls', namespace='tests')),
]

urlpatterns += swagger_patterns
