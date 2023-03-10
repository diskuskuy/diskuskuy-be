# from django.shortcuts import render
# from django.http import JsonResponse

# Create your views here.
from rest_framework import viewsets

from .serializers import *
from .models import *

class InitialPostViewSet(viewsets.ModelViewSet):
    queryset = InitialPost.objects.all()
    serializer_class = InitialPostSerializer

class ReplyPostViewSet(viewsets.ModelViewSet):
    queryset = ReplyPost.objects.all()
    serializer_class = ReplyPostSerializer

class NestedReplyPostViewSet(viewsets.ModelViewSet):
    queryset = NestedReplyPost.objects.all()
    serializer_class = NestedReplyPostSerializer