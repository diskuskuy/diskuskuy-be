from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .serializers import *
from .models import *

# handle request
class ThreadViewSet(viewsets.ModelViewSet):
    def list(self, request):
        queryset = Thread.objects.all()
        serializer_class = ThreadSerializer(queryset, many=True)
        return Response(serializer_class.data)

class ReferenceFileViewSet(viewsets.ModelViewSet):
    queryset = ReferenceFile.objects.all()
    serializer_class = ReferenceFileSerializer

class SummaryViewSet(viewsets.ModelViewSet):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer

class DiscussionGuideViewSet(viewsets.ModelViewSet):
    queryset = DiscussionGuide.objects.all()
    serializer_class = DiscussionGuideSerializer

class InquiryPhaseViewSet(viewsets.ModelViewSet):
    queryset = InquiryPhase.objects.all()
    serializer_class = InquiryPhaseSerializer
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
