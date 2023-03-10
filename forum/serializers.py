from rest_framework import serializers

from .models import Thread, Week


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        fields = '__all__'

class WeekSerializer(serializers.ModelSerializer):
    threads = ThreadSerializer(read_only=True, many=True)
    class Meta:
        model = Week
        fields = '__all__'