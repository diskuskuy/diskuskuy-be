from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .serializers import ThreadSerializer, WeekSerializer
from .models import Thread, Week

# handle request
class ThreadViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Thread.objects.all()
        serializer = ThreadSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Thread.objects.all()
        thread = get_object_or_404(queryset, pk=pk)
        serializer = ThreadSerializer(thread)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        queryset = Thread.objects.all()
        thread = get_object_or_404(queryset, pk=pk)
        serializer = ThreadSerializer(thread, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class WeekViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = WeekSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(serializer)
        return Response(serializer.data)

    def list(self, request):
        queryset = Week.objects.all()
        serializer = WeekSerializer(queryset, many=True)
        return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Week.objects.all()
    #     week = get_object_or_404(queryset, pk=pk)
    #     serializer = WeekSerializer(week)
    #     return Response(serializer.data)
    
    # def update(self, request, pk=None):
    #     queryset = Week.objects.all()
    #     week = get_object_or_404(queryset, pk=pk)
    #     serializer = WeekSerializer(week, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
