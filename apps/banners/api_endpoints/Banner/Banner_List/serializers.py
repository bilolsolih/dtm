from rest_framework.serializers import ModelSerializer

from apps.banners.models import Banner


class BannerListSerializer(ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id', 'title', 'subtitle', 'picture']
