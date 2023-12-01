from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.tests.models import Attempt
from .serializers import AttemptListSerializer


class AttemptListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AttemptListSerializer

    def get_queryset(self):
        queryset = Attempt.objects.filter(student=self.request.user)
        return queryset


__all__ = ['AttemptListAPIView']
