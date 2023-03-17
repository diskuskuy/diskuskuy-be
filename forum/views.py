from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import *

# handle request

class WeekViewSet(viewsets.ModelViewSet):
    queryset = Week.objects.all()
    serializer_class = WeekSerializer

class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Thread.objects.all()
    serializer_class = ThreadRequestSerializer

class ReferenceFileViewSet(viewsets.ModelViewSet):
    queryset = ReferenceFile.objects.all()
    serializer_class = ReferenceFileRequestSerializer

class SummaryViewSet(viewsets.ModelViewSet):
    queryset = Summary.objects.all()
    serializer_class = SummarySerializer

class DiscussionGuideViewSet(viewsets.ModelViewSet):
    queryset = DiscussionGuide.objects.all()
    serializer_class = DiscussionGuideRequestSerializer

class DiscussionAnalytics(APIView):

    def get(self, request):
        thread_id = request.query_params.get('thread_id')

        replies, tags, tags_nested = [], [], []
        total_participants, non_participants, nested_replies_count = 0, 0, 0
        temp = {}

        if thread_id is not None:
            initial_post = get_object_or_404(InitialPost.objects.all(), thread=thread_id)
            replies = ReplyPost.objects.filter(initial_post=initial_post.id)
            
            for reply in replies:
                nested_replies_count += NestedReplyPost.objects.filter(reply_post=reply.id).count()

            tags = ReplyPost.objects.values_list('tag').annotate(the_count=Count("tag"))
            tags_nested = NestedReplyPost.objects.values_list('tag').annotate(the_count=Count("tag"))
            for tag in tags:
                if tag[0] not in temp.keys():
                    temp[tag[0]] = tag[1]
                else:
                    temp[tag[0]] += tag[1]

            for tag in tags_nested:
                if tag[0] not in temp.keys():
                    temp[tag[0]] = tag[1]
                else:
                    temp[tag[0]] += tag[1]

        return Response(DiscussionAnalyticsSerializer({
            "replies": replies.count() + nested_replies_count, 
            "total_participants": total_participants, 
            "non_participants": non_participants,
            "tags": temp
            }).data)

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
