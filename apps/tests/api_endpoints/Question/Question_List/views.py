from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.tests.models import Question
from .serializers import QuestionListSerializer


class QuestionListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionListSerializer

    def get_queryset(self):
        queryset = Question.objects.all()
        return queryset


__all__ = ['QuestionListAPIView']
