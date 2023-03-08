from rest_framework import viewsets

from .serializers import ThreadSerializer, WeekSerializer
from .models import Thread, Week


class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer

class WeekViewSet(viewsets.ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer