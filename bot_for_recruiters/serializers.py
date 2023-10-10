from rest_framework import serializers

class ScrapeRequestSerializer(serializers.Serializer):
    url = serializers.URLField()
