from rest_framework import serializers

from .models import *
from forum.models import Thread

class NestedReplyPostRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = NestedReplyPost
        fields = '__all__'

class NestedReplyPostResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = NestedReplyPost
        fields = ('id', 'tag', 'content', 'date')        

class ReplyPostRequestSerializer(serializers.ModelSerializer):
    nested_reply_post = NestedReplyPostResponseSerializer(read_only=True, many=True)
    class Meta:
        model = ReplyPost
        fields = '__all__'

class ReplyPostResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReplyPost
        fields = ('id','tag','content','date')

class InitialPostSerializer(serializers.ModelSerializer):
    reply_post = ReplyPostResponseSerializer(read_only=True, many=True)
    class Meta:
        model = InitialPost
        fields = '__all__'

class InitialPostThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialPost
        fields = ('id', 'tag', 'content', 'date')
