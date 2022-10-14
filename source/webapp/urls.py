from django.urls import path
from webapp.views.index import IndexView
from webapp.views.task import TaskCreateView, TaskDetailView, TaskUpdateView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('task/create', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/detail', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_update')
]
