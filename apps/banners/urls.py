from django.urls import path

from . import api_endpoints as views

app_name = 'banners'

urlpatterns = [
    path('banner/list/', views.BannerListAPIView.as_view(), name='banner_list'),
]
