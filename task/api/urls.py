from django.contrib import admin
from django.urls import path, include, re_path

from .views import TaskApiList, TaskApiCreate, TaskApiUpdate, TaskApiDestroy
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'task', TaskViewSet, basename='task')

urlpatterns = [
    path('list/', TaskApiList.as_view()),
    path('create/', TaskApiCreate.as_view()),
    path('update/', TaskApiUpdate.as_view()),
    path('delete/<int:pk>', TaskApiDestroy.as_view()),
    path('auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
