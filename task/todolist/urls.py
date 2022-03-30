from django.contrib import admin
from django.urls import path, include

from .views import TaskIndex, TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'task', TaskViewSet, basename='task')

urlpatterns = [
    path('', TaskIndex.as_view()),
    path('api/', include(router.urls))
]
