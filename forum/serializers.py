from rest_framework import serializers
from .models import *
from post.serializers import *
from django.shortcuts import get_object_or_404
from datetime import datetime

class ReferenceFileRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceFile
        fields = '__all__'

class ReferenceFileResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceFile
        fields = ('id','title', 'url')

class SummaryRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'

class SummaryResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = ('id','content')

class DiscussionGuideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionGuide
        fields = '__all__'

class DiscussionGuideStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionGuide
        fields = ('id','state')

class DiscussionGuideResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionGuide
        fields = ('id','deadline','description','mechanism_expectation', 'state')

class ThreadRequestSerializer(serializers.ModelSerializer):
    initial_post = InitialPostThreadSerializer()
    reference_file = ReferenceFileResponseSerializer(read_only=True, many=True)
    summary = SummaryResponseSerializer(read_only=True)
    discussion_guide = DiscussionGuideResponseSerializer(read_only=True)
    
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

    def update(self, instance, validated_data):
        initial_post_data = validated_data.pop('initial_post')
        initial_post = instance.initial_post
        instance.title = validated_data.get('title', instance.title)
        instance.save()

        initial_post.tag = initial_post_data.get('tag', initial_post.tag)
        initial_post.content = initial_post_data.get('content', initial_post.content)
        initial_post.save()
        return instance

class ThreadResponseSerializer(serializers.ModelSerializer): #buat tampilan di week
    class Meta:
        model = Thread
        fields = ('id','title')

class WeekSerializer(serializers.ModelSerializer):
    threads = ThreadResponseSerializer(read_only=True, many=True)
    class Meta:
        model = Week
        fields = ('id','name','threads')