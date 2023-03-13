from rest_framework import serializers

from .models import *

class ReferenceFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceFile
        fields = '__all__'

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'

class InquiryPhaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InquiryPhase
        fields = '__all__'

class DiscussionGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionGuide
        fields = '__all__'

class ThreadSerializer(serializers.ModelSerializer):
    referenceFile = ReferenceFileSerializer(read_only=True, many=True)
    summary = SummarySerializer(read_only=True, many=True)
    initial_post = InitialPostSerializer(read_only=True, many=True)
    class Meta:
        model = Thread
        fields = '__all__'

class WeekSerializer(serializers.ModelSerializer):
    threads = ThreadSerializer(read_only=True, many=True)
    class Meta:
        model = Week
        fields = '__all__'