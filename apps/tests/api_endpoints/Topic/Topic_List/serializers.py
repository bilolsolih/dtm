from rest_framework.serializers import ModelSerializer

from apps.tests.models import Topic


class TopicListSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title']
