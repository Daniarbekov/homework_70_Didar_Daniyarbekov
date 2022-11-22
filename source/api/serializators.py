from rest_framework import serializers
from webapp.models import Task, Project, Type, Status


class ProjectSerializator(serializers.ModelSerializer):
    tasks = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = Project
        fields = ['id','name','description', 'start_date', 'end_date','updated_at','created_at','tasks']
        read_only_fields = ['id','updated_at', 'created_at','tasks']


class TaskSerializator(serializers.ModelSerializer):
    project = ProjectSerializator(read_only=True)
    type = serializers.SlugRelatedField(
        many=True,
        queryset = Type.objects.all(),
        slug_field='name')
    status = serializers.SlugRelatedField(queryset = Status.objects.all(),slug_field='name')
    
    class Meta:
        model = Task
        fields = ['id','summary','description', 'status', 'type', 'status','project','updated_at','created_at']
        read_only_fields = ['id','updated_at', 'created_at','project']
