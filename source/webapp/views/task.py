from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from webapp.forms import TaskForm
from webapp.models import Task
from django.urls import reverse_lazy


class TaskCreateView(CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    

class TaskUpdateView(UpdateView): 
    model = Task
    template_name = 'task_update.html'
    form_class = TaskForm


class TaskDeleteView(DeleteView): 
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('index')
