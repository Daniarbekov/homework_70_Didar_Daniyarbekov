from django.urls import path
from api.views import ProjectDetailView


urlpatterns = [
    path('project/<int:pk>', ProjectDetailView.as_view()),
]