from django.urls import path
from post.views import test
# from django.views.generic import TemplateView

urlpatterns = [
    # # Miscellaneous
    # path('discussion_phases/', TemplateView.as_view(template_name='discussion/discussion_phases.html'), name='discussion_phases'),
    # # Thread CRUD
    # path('thread/list/', ThreadListView.as_view(), name='thread_list'),
    # path('thread/add/', ThreadCreateView.as_view(), name='thread_add'),
    # path('thread/<int:pk>/', ThreadDetailView.as_view(), name='thread_detail'),
    # path('thread/<int:pk>/edit/', ThreadUpdateView.as_view(), name='thread_edit'),
    # path('thread/<int:pk>/delete/', ThreadDeleteView.as_view(), name='thread_delete'),
    # # Resources CRUD
    # path('resource/list/', ResourceListView.as_view(), name='resource_list'),
    # path('resource/add/', ResourceCreateView.as_view(), name='resource_add'),
    # path('resource/<int:pk>/', ResourceDetailView.as_view(), name='resource_detail'),
    # path('resource/<int:pk>/edit/', ResourceUpdateView.as_view(), name='resource_edit'),
    # path('resource/<int:pk>/delete/', ResourceDeleteView.as_view(), name='resource_delete'),
    path('', test, name='post'),

]