from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from webapp.models import Project
from webapp.forms import ProjectForm


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