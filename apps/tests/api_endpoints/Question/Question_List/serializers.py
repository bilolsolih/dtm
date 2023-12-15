from rest_framework.serializers import ModelSerializer

from apps.tests.models import Question, QuestionType


class QuestionTypeInQuestionListSerializer(ModelSerializer):
    class Meta:
        model = QuestionType
        fields = ['id', 'title', 'prompt']


class QuestionListSerializer(ModelSerializer):
    type = QuestionTypeInQuestionListSerializer(many=False)

    class Meta:
        model = Question
        fields = ['id', 'type', 'question', 'picture']
