from django.db import models
from tinymce.models import HTMLField 
from django.contrib.auth.models import User
from forum.models import Thread
from datetime import datetime

class InitialPost(models.Model):
    tag = models.CharField(max_length=100, default="Pemicu")
    content = HTMLField(default=" ")
    date = models.DateTimeField(auto_now=True, editable=False)
    thread = models.OneToOneField(Thread, on_delete=models.CASCADE, default=1, related_name="initial_post")
    # lecturer = 
    # likes = models.ManyToManyField(User, blank=True, related_name='likes')
    # user = 

    def __str__(self):
        return self.content

    # def number_of_likes(self):
    #     return self.likes.count()

class ReplyPost(models.Model):
    tag = models.CharField(max_length=100, default="Pendapat")
    content = HTMLField(default=" ")
    date = models.DateTimeField(auto_now=True, editable=False)
    initial_post = models.ForeignKey(InitialPost, on_delete=models.CASCADE, related_name="reply_post")
    # user = 
    # likes = models.ManyToManyField(User, blank=True, related_name='likes')
    # user = 

    def __str__(self):
        return self.content

    # def number_of_likes(self):
    #     return self.likes.count()

class NestedReplyPost(models.Model):
    tag = models.CharField(max_length=100, default="Pendapat")
    content = HTMLField(default=" ")
    date = models.DateTimeField(auto_now=True, editable=False)
    reply_post = models.ForeignKey(ReplyPost, on_delete=models.CASCADE, related_name="nested_reply_post")
    # likes = models.ManyToManyField(User, blank=True, related_name='likes')
    # user = 

    def __str__(self):
        return self.content

    # def number_of_likes(self):
    #     return self.likes.count()

