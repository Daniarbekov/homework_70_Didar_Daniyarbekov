from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import DetailView
from webapp.forms import TaskForm
from webapp.models import Task


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
