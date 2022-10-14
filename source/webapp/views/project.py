from django.views.generic import ListView, DetailView
from webapp.models import Project


class ProjectListView(ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    template_name = 'project/detail.html'
    model = Project
