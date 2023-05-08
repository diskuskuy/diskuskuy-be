from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('initialpost', views.InitialPostViewSet)
router.register('replypost', views.ReplyPostViewSet)
router.register('nestedreplypost', views.NestedReplyPostViewSet)
router.register('post', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('reaction/<int:pk>/', views.PostReactionViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='post'))
]