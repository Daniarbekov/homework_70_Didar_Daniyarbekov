from django.views.generic.edit import CreateView
from webapp.forms import TaskForm


class TaskCreateView(CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm
