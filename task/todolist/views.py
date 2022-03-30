from rest_framework import generics, viewsets
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.generic import ListView

from .models import Task
from .serializers import TaskSerializer


class TaskIndex(ListView):
    model = Task
    template_name = 'todolist/index.html'
    context_object_name = 'tasks'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ToDo'
        return context




class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Task.objects.all()

        else:
            return Task.objects.filter(pk=pk)


