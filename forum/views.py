from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .serializers import *
from .models import *

# handle request
class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadRequestSerializer

class WeekViewSet(viewsets.ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer