from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from webapp.forms import TaskForm
from webapp.models import Task, Project
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


class TaskCreateView(CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm
    
    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)


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
