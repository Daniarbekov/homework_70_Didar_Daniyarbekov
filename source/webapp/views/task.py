from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from webapp.forms import TaskForm
from webapp.models import Task, Project
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskCreateView(LoginRequiredMixin,CreateView):
    template_name = 'task_create.html'
    form_class = TaskForm
    
    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        form.instance.project = project
        return super().form_valid(form)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'

    def get_object(self, **kwargs):
        object = Task.objects.get(pk=self.kwargs.get('pk'))
        if object.is_deleted == True:
            raise Http404
        return object


class TaskUpdateView(LoginRequiredMixin,UpdateView): 
    model = Task
    template_name = 'task_update.html'
    form_class = TaskForm


class TaskDeleteView(LoginRequiredMixin,DeleteView): 
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('index')
