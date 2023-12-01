from rest_framework.generics import ListAPIView

from apps.banners.models import Banner
from .serializers import BannerListSerializer


class BannerListAPIView(ListAPIView):
    serializer_class = BannerListSerializer

    def get_queryset(self):
        queryset = Banner.objects.filter(is_active=True)
        return queryset


__all__ = ['BannerListAPIView']
