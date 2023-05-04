from rest_framework import serializers

from .models import *

class PostSerializer(serializers.ModelSerializer):
    creator_name = serializers.ReadOnlyField()
    creator_photo = serializers.ReadOnlyField()
    creator_role = serializers.ReadOnlyField()
    number_of_likes = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {'creator': {'write_only': True}}

class NestedReplyPostSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = NestedReplyPost
        fields = '__all__'
        extra_kwargs = {'reply_post': {'write_only': True}}

# class NestedReplyPostResponseSerializer(serializers.ModelSerializer):
#     post = PostSerializer(read_only=True)

#     class Meta:
#         model = NestedReplyPost
#         fields = ('id', 'post')        

class ReplyPostSerializer(serializers.ModelSerializer):
    nested_reply_post = NestedReplyPostSerializer(read_only=True, many=True)
    post = PostSerializer()

    class Meta:
        model = ReplyPost
        fields = '__all__'
        extra_kwargs = {'initial_post': {'write_only': True}}

# class ReplyPostResponseSerializer(serializers.ModelSerializer):
#     post = PostSerializer(read_only=True)

#     class Meta:
#         model = ReplyPost
#         fields = ('id', 'post')

class InitialPostSerializer(serializers.ModelSerializer):
    reply_post = ReplyPostSerializer(read_only=True, many=True)
    post = PostSerializer()

    class Meta:
        model = InitialPost
        fields = '__all__'
        extra_kwargs = {'thread': {'write_only': True}}

# class InitialPostThreadSerializer(serializers.ModelSerializer):
#     post = PostSerializer(read_only=True)

#     class Meta:
#         model = InitialPost
#         fields = ('id', 'post')
