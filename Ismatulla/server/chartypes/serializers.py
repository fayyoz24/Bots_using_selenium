# myapp/serializers.py

from rest_framework import serializers


class CharacterSerializer(serializers.Serializer):
    character = serializers.CharField()

class QuestionSerializer(serializers.Serializer):
    sum_chars = serializers.IntegerField()