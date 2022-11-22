from django.urls import path
from api.views import ProjectDetailView, TaskDetailView


urlpatterns = [
    path('project/<int:pk>', ProjectDetailView.as_view()),
    path("task/<int:pk>", TaskDetailView.as_view()),
]
