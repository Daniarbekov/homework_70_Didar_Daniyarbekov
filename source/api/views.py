from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializators import ProjectSerializator
from webapp.models import Project
from django.shortcuts import get_object_or_404


class ProjectDetailView(APIView):
    def get(self, request, pk, format=None):
        project = get_object_or_404(Project,pk=pk)
        serializer = ProjectSerializator(project)
        return Response(serializer.data)
