from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

router = routers.DefaultRouter()
router.register('Week', views.WeekViewSet)
router.register('Thread', views.ThreadViewSet)
router.register('ReferenceFile', views.ReferenceFileViewSet)
router.register('Summary', views.SummaryViewSet)
router.register('DiscussionGuide', views.DiscussionGuideViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('analytics/', views.DiscussionAnalytics.as_view(), name="analytics"),
    path('update-state/<int:pk>/', views.discussion_guide_update_state),
]
