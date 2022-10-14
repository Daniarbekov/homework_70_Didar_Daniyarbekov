from django.urls import path
from webapp.views.index import IndexView
from webapp.views.task import TaskCreateView

urlpatterns = [
    path("", IndexView.as_view(), name='index'),
    path('task/create', TaskCreateView.as_view(), name='task_create')
]
