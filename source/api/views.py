from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializators import ProjectSerializator, TaskSerializator
from webapp.models import Project, Task
from django.shortcuts import get_object_or_404


class ProjectDetailView(APIView):
    def get(self, request, pk, format=None):
        project = get_object_or_404(Project,pk=pk)
        serializer = ProjectSerializator(project)
        return Response(serializer.data)


class TaskDetailView(APIView):
    def get(self, request, pk, format=None):
        task = get_object_or_404(Task,pk=pk)
        serializer = TaskSerializator(task)
        return Response(serializer.data)
