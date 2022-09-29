from rest_framework import serializers

from .models import Category, QuestionAnswer


class CategorySerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = "__all__"


class QuestionAnswerSerializer(serializers.ModelSerializer):
    questionanswer_question = serializers.ReadOnlyField()

    class Meta:
        model = QuestionAnswer
        fields = "__all__"
