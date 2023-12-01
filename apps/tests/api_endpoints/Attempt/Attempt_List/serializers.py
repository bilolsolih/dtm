from rest_framework.serializers import ModelSerializer

from apps.tests.models import Attempt


class AttemptListSerializer(ModelSerializer):
    class Meta:
        model = Attempt
        fields = ['id', 'subject', 'topic', 'created']
