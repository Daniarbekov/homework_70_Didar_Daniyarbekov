from django.urls import path
from api.views import ProjectDetailView, TaskDetailView, ProjectUpdateView, TaskUpdateView


urlpatterns = [
    path('project/<int:pk>', ProjectDetailView.as_view()),
    path("task/<int:pk>", TaskDetailView.as_view()),
    path('project/<int:pk>/update', ProjectUpdateView.as_view()),
    path('task/<int:pk>/update', TaskUpdateView.as_view()),
]