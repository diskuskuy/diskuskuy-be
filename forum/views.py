from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework.decorators import action

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
