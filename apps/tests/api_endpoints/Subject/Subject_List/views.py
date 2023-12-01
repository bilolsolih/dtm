from rest_framework.generics import ListAPIView

from apps.tests.models import Subject
from .serializers import SubjectListSerializer


class SubjectListAPIView(ListAPIView):
    serializer_class = SubjectListSerializer

    def get_queryset(self):
        queryset = Subject.objects.filter(is_active=True)
        return queryset


__all__ = ['SubjectListAPIView']
