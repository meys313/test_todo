from django.contrib import admin
from django.urls import path

from .views import TaskIndex



urlpatterns = [
    path('', TaskIndex.as_view()),
]
