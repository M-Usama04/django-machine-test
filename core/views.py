from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Client, Project
from .serializers import *
from .utils import success_response, error_response
from .serializers import ClientSerializer, ClientDetailSerializer
from rest_framework import viewsets

class ClientListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Client.objects.all().order_by('-created_at')

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return ClientCreateSerializer
        return ClientSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            client = serializer.save(created_by=request.user)
            response_data = ClientSerializer(client).data
            return success_response("Client created successfully", response_data, status.HTTP_201_CREATED)
        return error_response("Client creation failed", status.HTTP_400_BAD_REQUEST)

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = ClientCreateSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return success_response("Client updated successfully", ClientSerializer(instance).data)
        return error_response("Client update failed")

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return success_response("Client deleted successfully", code=status.HTTP_204_NO_CONTENT)

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
            response_data = ProjectDetailSerializer(project).data
            return success_response("Project created successfully", response_data, status.HTTP_201_CREATED)
        return error_response("Project creation failed")

class UserProjectsView(generics.ListAPIView):
    serializer_class = ProjectDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.projects_assigned.all().order_by('-created_at')
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClientDetailSerializer
        return ClientSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(updated_at=timezone.now())
