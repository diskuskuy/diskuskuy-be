from forum.models import Thread
from rest_framework import viewsets
from forum.serializers import ThreadSerializer
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import (
    GetThreadRequest,
	GetThreadResponse,
	CreateThreadRequest,
	CreateThreadResponse,
	ThreadSerializer,
)

from .services import (
	ThreadService
)

from .specs import (
	CreateThreadSpec
)

class ThreadViewSet(viewsets.ModelViewSet):
	queryset = Thread.objects.all()
	serializer_class = ThreadSerializer

	@action(detail=False, url_path="get", methods=["get"])
	def get_thread(self, request: Request) -> Response:
		"""
		Get single thread object by id
		"""
		serializer = GetThreadRequest(data=request.query_params)
		serializer.is_valid(raise_exception=True)
		data = serializer.data
		thread = ThreadService.get_thread(data["id"])
		return Response(GetThreadResponse({"data": thread}).data)

	@action(
		detail=False,
		url_path="create",
		methods=["post"],
	)
	def create_thread(self, request: Request) -> Response:
		serializer = CreateThreadRequest(data=request.data)
		serializer.is_valid(raise_exception=True)
		data = serializer.data
		spec = CreateThreadSpec(
			week_id=data["week_id"],
			title=data["title"],
		)
		thread = ThreadService.create_thread(spec)
		return Response(CreateThreadResponse({"data": thread}).data)


