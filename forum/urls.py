from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('Thread', views.ThreadViewSet)
router.register('Week', views.WeekViewSet)
# router.register('DiscussionGuide', views.DiscussionGuideViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]