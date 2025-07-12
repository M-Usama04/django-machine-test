from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProjectNestedSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='project_name')

    class Meta:
        model = Project
        fields = ['id', 'name']

class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username')
    projects = ProjectNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'updated_at', 'created_by']

class ClientCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['client_name']

class ProjectDetailSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.client_name')
    users = UserSimpleSerializer(many=True)
    created_by = serializers.CharField(source='created_by.username')

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_by', 'created_at']

class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['project_name', 'users']
class ClientDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    projects = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'projects', 'created_at', 'created_by', 'updated_at']

    def get_projects(self, obj):
        return [
            {
                "id": project.id,
                "name": project.project_name
            }
            for project in obj.projects.all()
        ]
class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.client_name', read_only=True)
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    users = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_at', 'created_by']

    def get_users(self, obj):
        return [
            {"id": user.id, "name": user.username}
            for user in obj.users.all()
        ]
