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
    
    # def create(self, validated_data):
    #     reply_post_data = validated_data('reply_post')
    #     initial_post = InitialPost.objects.create(**validated_data)
    #     for reply_post_data in reply_post:
    #         ReplyPost.objects.create(initial_post=initial_post, **reply_post_data)
    #     return initial_post


# class PostSerializer(serializers.ModelSerializer):
#     initial_post = InitialPostSerializer(required=True)
#     class Meta:
#         model = Post
#         fields = '__all__'
    
#     def create(self, validated_data):
#         initial_post_data = validated_data('initial_post')
#         post = Post.objects.create(**validated_data)
#         for initial_post_data in initial_post:
#             InitialPost.objects.create(post=post, **initial_post_data)
#         return post


    
    # def create(self, validate_data):
    #     post_data = validate_data.pop('post')
    #     post = PostSerializer.create(PostSerializer(), validate_data=post_data)
    #     initial_post, created = InitialPost.objects.update_or_create(post=post, thread=validate_data.pop('thread'))
    #     return initial_post

# class ReplyPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ReplyPost
#         fields = '__all__'

# class NestedReplyPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = NestedReplyPost
#         fields = '__all__'