from forum.models import Thread
from rest_framework import serializers

class ThreadSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)
    title = serializers.CharField()
    week_id = serializers.IntegerField(min_value=1)

class GetThreadRequest(serializers.Serializer):
    id = serializers.IntegerField(min_value=1)

class GetThreadResponse(serializers.Serializer):
    data = ThreadSerializer()

class CreateThreadRequest(serializers.Serializer):
    title = serializers.CharField(required=True)
    week_id = serializers.IntegerField(min_value=1)

class CreateThreadResponse(serializers.Serializer):
    data = ThreadSerializer()


