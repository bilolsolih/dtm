from rest_framework.serializers import ModelSerializer

from apps.tests.models import TestCategory


class TestCategoryListSerializer(ModelSerializer):
    class Meta:
        model = TestCategory
        fields = ['id', 'title', 'description']
