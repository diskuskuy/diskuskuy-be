from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('profile', views.CustomUserView)

urlpatterns = [
    path('', include(router.urls)),
    path('login', views.LoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
]