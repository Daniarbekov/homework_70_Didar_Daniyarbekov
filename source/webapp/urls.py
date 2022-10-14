from django.urls import path
from webapp.views.index import IndexView
from webapp.views.task import TaskCreateView, TaskDetailView, TaskUpdateView, TaskDeleteView
from webapp.views.project import ProjectListView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('task/create', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/detail', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
    path('projects', ProjectListView.as_view(), name='projects'),
    path('projects/<int:pk>', ProjectDetailView.as_view(), name='project_detail'),
    path('projects/create', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'), 
    path('projects/<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete'), 
]
