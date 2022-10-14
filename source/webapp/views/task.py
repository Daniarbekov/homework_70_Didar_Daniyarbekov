from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from webapp.forms import TaskForm
from webapp.models import Task


class TaskCreateView(CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
