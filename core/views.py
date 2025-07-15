from rest_framework import status, viewsets, generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Client, Project
from .serializers import *
from .utils import success_response, error_response


class ClientViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all().order_by('-created_at')

    def get_serializer_class(self):
        return ClientCreateSerializer if self.action in ['create', 'update', 'partial_update'] else ClientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            client = serializer.save()
            return success_response("Client created successfully", ClientSerializer(client).data, status.HTTP_201_CREATED)
        return error_response("Client creation failed", serializer.errors)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return success_response("Client list fetched successfully", serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ClientSerializer(instance)
        return success_response("Client retrieved", serializer.data)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ClientCreateSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            updated_instance = serializer.save()
            return success_response("Client updated", ClientSerializer(updated_instance).data)
        return error_response("Client update failed", serializer.errors)

    def destroy(self, request, *args, **kwargs):
        self.get_object().delete()
        return success_response("Client deleted", code=status.HTTP_204_NO_CONTENT)


class ProjectCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        client = get_object_or_404(Client, pk=pk)
        serializer = ProjectCreateSerializer(data=request.data)
        if serializer.is_valid():
            project = Project.objects.create(
                project_name=serializer.validated_data['project_name'],
                client=client,
                created_by=request.user
            )
            project.users.set(serializer.validated_data['users'])
            return success_response("Project created successfully", ProjectDetailSerializer(project).data, status.HTTP_201_CREATED)
        return error_response("Project creation failed", serializer.errors)


class UserProjectsView(generics.ListAPIView):
    serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.projects_assigned.all().order_by('-created_at')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return success_response("Projects assigned to user fetched", serializer.data)
