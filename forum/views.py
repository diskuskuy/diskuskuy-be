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

class ReferenceFileViewSet(viewsets.ModelViewSet):
    queryset = ReferenceFile.objects.all()
    serializer_class = ReferenceFileSerializer

class SummaryViewSet(viewsets.ModelViewSet):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer

class DiscussionGuideViewSet(viewsets.ModelViewSet):
    queryset = DiscussionGuide.objects.all()
    serializer_class = DiscussionGuideSerializer

# class InquiryPhaseViewSet(viewsets.ModelViewSet):
#     queryset = InquiryPhase.objects.all()
#     serializer_class = InquiryPhaseSerializer
#     def retrieve(self, request, pk=None):
#         queryset = Thread.objects.all()
#         thread = get_object_or_404(queryset, pk=pk)
#         serializer = ThreadSerializer(thread)
#         return Response(serializer.data)
    
#     def update(self, request, pk=None):
#         queryset = Thread.objects.all()
#         thread = get_object_or_404(queryset, pk=pk)
#         serializer = ThreadSerializer(thread, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
