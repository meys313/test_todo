from rest_framework import generics, viewsets
from todolist.models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            return Task.objects.all()

        else:
            return Task.objects.filter(pk=pk)
