from rest_framework.generics import ListAPIView

from apps.tests.models import TestCategory
from .serializers import TestCategoryListSerializer


class TestCategoryListAPIView(ListAPIView):
    serializer_class = TestCategoryListSerializer

    def get_queryset(self):
        queryset = TestCategory.objects.all()
        return queryset


__all__ = ['TestCategoryListAPIView']
