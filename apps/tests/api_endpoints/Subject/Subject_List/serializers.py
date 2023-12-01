from rest_framework.serializers import ModelSerializer

from apps.tests.models import Subject


class SubjectListSerializer(ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title']
