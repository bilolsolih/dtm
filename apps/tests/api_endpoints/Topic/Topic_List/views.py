import django_filters
from django_filters.filterset import FilterSet
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from apps.tests.models import Topic, Subject
from .serializers import TopicListSerializer


class TopicFilterSet(FilterSet):
    subject = django_filters.ModelChoiceFilter(field_name='subject', to_field_name='pk', queryset=Subject.objects.filter(is_active=True))


class TopicListAPIView(ListAPIView):
    serializer_class = TopicListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TopicFilterSet

    def get_queryset(self):
        queryset = Topic.objects.all()
        return queryset


__all__ = ['TopicListAPIView']
