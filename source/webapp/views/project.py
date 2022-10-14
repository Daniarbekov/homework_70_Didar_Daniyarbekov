from django.views.generic import ListView
from webapp.models import Project


class ProjectListView(ListView):
    template_name = 'projects.html'
    model = Project
    context_object_name = 'projects'
