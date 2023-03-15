from rest_framework import serializers
from .models import *
from post.serializers import *
from django.shortcuts import get_object_or_404

class ReferenceFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceFile
        fields = '__all__'

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'

class DiscussionGuideSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionGuide
        fields = '__all__'

class DiscussionGuideStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionGuide
        fields = ('id','state')

class ThreadRequestSerializer(serializers.ModelSerializer):
    initial_post = InitialPostThreadSerializer()
    reference_file = ReferenceFileSerializer(read_only=True, many=True)
    summary = SummarySerializer(read_only=True)
    discussion_guide = DiscussionGuideSerializer(read_only=True)
    
    class Meta:
        model = Thread
        fields = '__all__'
    
    def create(self, validated_data):
        week = get_object_or_404(Week.objects.all(), pk=validated_data['week'].id)
        thread = Thread(
            title=validated_data['title'],
            week=week
        )
        thread.save()
        initial_post = InitialPost(
            tag=validated_data['initial_post']['tag'],
            content=validated_data['initial_post']['content'],
            thread=thread
        )
        initial_post.save()
        return thread

    # def update():


class ThreadResponseSerializer(serializers.ModelSerializer): #buat tampilan di week
    class Meta:
        model = Thread
        fields = ('id','title')

class WeekSerializer(serializers.ModelSerializer):
    threads = ThreadResponseSerializer(read_only=True, many=True)
    class Meta:
        model = Week
        fields = ('id','name','threads')