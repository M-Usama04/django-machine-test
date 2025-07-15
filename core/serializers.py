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

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user if request else None
        if not user:
            raise serializers.ValidationError("User is required to create client.")
        return Client.objects.create(created_by=user, **validated_data)

class ProjectDetailSerializer(serializers.ModelSerializer):
    client = serializers.CharField(source='client.client_name')
    users = UserSimpleSerializer(many=True)
    created_by = serializers.CharField(source='created_by.username')

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'users', 'created_by', 'created_at', 'updated_at']

class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Project
        fields = ['project_name', 'users']
