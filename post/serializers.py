from rest_framework import serializers

from .models import *
from forum.models import Thread

class NestedReplyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = NestedReplyPost
        fields = '__all__'

class ReplyPostSerializer(serializers.ModelSerializer):
    nested_reply_post = NestedReplyPostSerializer(read_only=True, many=True)
    class Meta:
        model = ReplyPost
        fields = '__all__'

class InitialPostSerializer(serializers.ModelSerializer):
    reply_post = ReplyPostSerializer(read_only=True, many=True)
    class Meta:
        model = InitialPost
        fields = '__all__'

class InitialPostThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = InitialPost
        fields = ('id', 'tag', 'content', 'date')
