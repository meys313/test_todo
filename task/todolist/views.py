from django.views.generic import ListView

from .models import Task


class TaskIndex(ListView):
    model = Task
    template_name = 'todolist/index.html'
    context_object_name = 'tasks'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'ToDo'
        return context



