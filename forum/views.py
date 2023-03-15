from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

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

@api_view(['PUT'])
def discussion_guide_update_state(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        discussion_guide = DiscussionGuide.objects.get(pk=pk)
    except DiscussionGuide.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = DiscussionGuideStateSerializer(discussion_guide, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
