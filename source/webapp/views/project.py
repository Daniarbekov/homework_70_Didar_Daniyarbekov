from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from webapp.models import Project
from webapp.forms import ProjectForm
from django.urls import reverse_lazy


class ProjectListView(ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    template_name = 'project/detail.html'
    model = Project 


class ProjectCreateView(CreateView):
    template_name = 'project/create.html'
    form_class = ProjectForm


class ProjectUpdateView(UpdateView):
    model = Project
    template_name = 'project/update.html'
    form_class = ProjectForm


class ProjectDeleteView(DeleteView):
    template_name = 'project/delete.html'
    model = Project
    success_url = reverse_lazy('index')
