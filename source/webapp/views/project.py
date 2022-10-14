from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
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
