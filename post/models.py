from django.db import models
from tinymce.models import HTMLField 
from django.contrib.auth.models import User
from forum.models import Thread
from datetime import datetime

# Create your models here.
# class Post(models.Model):
#     title = models.CharField(max_length=100)
#     tag = models.CharField(max_length=100)
#     content = HTMLField()
#     date = models.DateTimeField(verbose_name="Deadline (MM/DD/YYYY)")
#     likes = models.ManyToManyField(User, blank=True, related_name='likes')
#     # user = 

#     def __str__(self):
#         return self.title

#     def number_of_likes(self):
#         return self.likes.count()

class InitialPost(models.Model):
    title = models.CharField(max_length=100, default="Title-1")
    tag = models.CharField(max_length=100, default="Pemicu")
    content = HTMLField(default=" ")
    date = models.DateTimeField(verbose_name="Deadline (MM/DD/YYYY)", default=datetime.now)
    # post = models.OneToOneField(Post, on_delete=models.CASCADE)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, default=1)
    # lecturer = 
    # likes = models.ManyToManyField(User, blank=True, related_name='likes')
    # user = 

    def __str__(self):
        return self.title

    # def number_of_likes(self):
    #     return self.likes.count()

class ReplyPost(models.Model):
    title = models.CharField(max_length=100, default="Title-1")
    tag = models.CharField(max_length=100, default="Pendapat")
    content = HTMLField(default=" ")
    date = models.DateTimeField(verbose_name="Deadline (MM/DD/YYYY)", default=datetime.now)
    # post = models.OneToOneField(Post, on_delete=models.CASCADE)
    initial_post = models.ForeignKey(InitialPost, on_delete=models.CASCADE)
    # user = 
    # likes = models.ManyToManyField(User, blank=True, related_name='likes')
    # user = 

    def __str__(self):
        return self.title

    # def number_of_likes(self):
    #     return self.likes.count()

class NestedReplyPost(models.Model):
    title = models.CharField(max_length=100, default="Title-1")
    tag = models.CharField(max_length=100, default="Pendapat")
    content = HTMLField(default=" ")
    date = models.DateTimeField(verbose_name="Deadline (MM/DD/YYYY)", default=datetime.now)
    # post = models.OneToOneField(Post, on_delete=models.CASCADE)
    reply_post = models.ForeignKey(ReplyPost, on_delete=models.CASCADE)
    # user = 
    
    # likes = models.ManyToManyField(User, blank=True, related_name='likes')
    # user = 

    def __str__(self):
        return self.title

    # def number_of_likes(self):
    #     return self.likes.count()

# class Reaction(models.Model):
