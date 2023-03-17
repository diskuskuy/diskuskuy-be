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
        read_only_fields = ['state']

class ThreadRequestSerializer(serializers.ModelSerializer):
    initial_post = InitialPostThreadSerializer()
    reference_file = ReferenceFileResponseSerializer(many=True)
    summary = SummaryResponseSerializer(read_only=True)
    discussion_guide = DiscussionGuideResponseSerializer()
    
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
        if 'initial_post' in validated_data:
            initial_post_data = validated_data.pop('initial_post')
            initial_post = instance.initial_post
            initial_post.tag = initial_post_data.get('tag', initial_post.tag)
            initial_post.content = initial_post_data.get('content', initial_post.content)
            initial_post.save()

        if 'reference_file' in validated_data:
            reference_file_data = validated_data.pop('reference_file')
            reference_file = ReferenceFile.objects.filter(thread=instance)
            for ref in reference_file:
                for ref_data in reference_file_data:
                    ref.title = ref_data.get('title', ref.title)
                    ref.url = ref_data.get('url', ref.url)
                ref.save()

        if 'discussion_guide' in validated_data:
            discussion_guide_data = validated_data.pop('discussion_guide')
            discussion_guide = instance.discussion_guide
            discussion_guide.deadline = discussion_guide_data.get('deadline', discussion_guide.deadline)
            discussion_guide.description = discussion_guide_data.get('description', discussion_guide.description)
            discussion_guide.mechanism_expectation = discussion_guide_data.get('mechanism_expectation', discussion_guide.mechanism_expectation)
            discussion_guide.save()

        instance.title = validated_data.get('title', instance.title)
        instance.save()

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

class DiscussionAnalyticsSerializer(serializers.Serializer):
    replies = serializers.IntegerField()
    total_participants = serializers.IntegerField()
    non_participants = serializers.IntegerField()
    tags = serializers.DictField()
