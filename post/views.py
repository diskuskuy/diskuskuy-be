# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .models import *

class InitialPostViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    queryset = InitialPost.objects.all()
    serializer_class = InitialPostSerializer

class ReplyPostViewSet(viewsets.ModelViewSet):    
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    queryset = ReplyPost.objects.all()
    serializer_class = ReplyPostSerializer

class NestedReplyPostViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    queryset = NestedReplyPost.objects.all()
    serializer_class = NestedReplyPostSerializer
