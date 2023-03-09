from django.db import models
from tinymce.models import HTMLField 
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    tag = models.CharField(max_length=100)
    content = HTMLField()
    date = models.DateTimeField(verbose_name="Deadline (MM/DD/YYYY)")
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    # user_id = 

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

class InitialPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    # thread = 
    # lecturer = 

class ReplyPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    initial_post = models.ForeignKey(InitialPost, on_delete=models.CASCADE)
    # user_id = 

class NestedReplyPost(models.Model):
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    reply_post = models.ForeignKey(ReplyPost, on_delete=models.CASCADE)
    # user = 

# class Reaction(models.Model):
