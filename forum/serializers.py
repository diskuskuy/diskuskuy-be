from rest_framework import serializers
from .models import *
from post.serializers import *
from django.shortcuts import get_object_or_404
from datetime import datetime

class ReferenceFileRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceFile
        fields = '__all__'

class ReferenceFileThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceFile
        fields = ('id','title', 'url')

class SummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Summary
        fields = '__all__'

class SummaryThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model=Summary
        fields=('id','content')

class DiscussionGuideRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionGuide
        fields = '__all__'

class DiscussionGuideStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionGuide
        fields = ('id','state')

class DiscussionGuideThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscussionGuide
        fields = ('id','deadline','description','mechanism_expectation')

class ThreadRequestSerializer(serializers.ModelSerializer):
    initial_post = InitialPostThreadSerializer()
    reference_file = ReferenceFileThreadSerializer(many=True)
    summary = SummaryThreadSerializer(read_only=True)
    discussion_guide = DiscussionGuideThreadSerializer()
    
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
        initial_post_data = validated_data['initial_post']
        initial_post = InitialPost(
            tag=initial_post_data['tag'],
            content=initial_post_data['content'],
            thread=thread
        )
        initial_post.save()
        discussion_guide_data = validated_data['discussion_guide']
        discussion_guide=DiscussionGuide(
            deadline=discussion_guide_data['deadline'],
            description=discussion_guide_data['description'],
            mechanism_expectation=discussion_guide_data['mechanism_expectation'],
            thread=thread
        )
        discussion_guide.save()
        reference_file_datas = validated_data['reference_file']
        for reference_file_data in reference_file_datas:
            reference_file=ReferenceFile(
                title=reference_file_data['title'],
                url=reference_file_data['url'],
                thread=thread
            )
            reference_file.save()
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
    threads = ThreadResponseSerializer(read_only=True,many=True)
    class Meta:
        model = Week
        fields = ('id','name','threads')

class DiscussionAnalyticsSerializer(serializers.Serializer):
    replies = serializers.IntegerField()
    total_participants = serializers.IntegerField()
    non_participants = serializers.IntegerField()
    tags = serializers.DictField()
    