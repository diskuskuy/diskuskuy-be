from rest_framework import serializers

from .models import Thread, Week
from post.serializers import InitialPostSerializer

class ThreadSerializer(serializers.ModelSerializer):
    initial_post = InitialPostSerializer(read_only=True, many=True)
    class Meta:
        model = Thread
        fields = '__all__'

class WeekSerializer(serializers.ModelSerializer):
    threads = ThreadSerializer(read_only=True, many=True)
    class Meta:
        model = Week
        fields = '__all__'