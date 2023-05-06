from rest_framework import serializers

from .models import *

class PostSerializer(serializers.ModelSerializer):
    creator_name = serializers.ReadOnlyField()
    creator_photo_url = serializers.ReadOnlyField()
    creator_role = serializers.ReadOnlyField()
    number_of_likes = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {'creator': {'write_only': True}}

class PostWeekSerializer(serializers.ModelSerializer):
    creator_name = serializers.ReadOnlyField()
    creator_photo_url = serializers.ReadOnlyField()

    class Meta:
        model = Post
        fields = ('creator_name', 'creator_photo_url')

class NestedReplyPostSerializer(serializers.ModelSerializer):
    post = PostSerializer()

    class Meta:
        model = NestedReplyPost
        fields = '__all__'

    def create(self, validated_data):
        reply_post = get_object_or_404(ReplyPost.objects.all(), pk=validated_data['reply_post'].id)
        post_data = validated_data['post']
        post = Post(
            tag=post_data['tag'],
            content=post_data['content'],
            creator=post_data['creator'],
        )
        post.save()
        nested_reply_post = NestedReplyPost(
            post=post,
            reply_post=reply_post
        )
        nested_reply_post.save()
        return nested_reply_post

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

    def create(self, validated_data):
        initial_post = get_object_or_404(InitialPost.objects.all(), pk=validated_data['initial_post'].id)
        post_data = validated_data['post']
        post = Post(
            tag=post_data['tag'],
            content=post_data['content'],
            creator=post_data['creator'],
        )
        post.save()
        reply_post = ReplyPost(
            post=post,
            initial_post=initial_post
        )
        reply_post.save()
        return reply_post

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

class InitialPostWeekThreadSerializer(serializers.ModelSerializer):
    post = PostWeekSerializer(read_only=True)

    class Meta:
        model = InitialPost
        fields = ['post']
