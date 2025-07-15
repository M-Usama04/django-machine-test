from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Client, Project

class MachineTestAPICases(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.force_authenticate(user=self.user)
        self.client_obj = Client.objects.create(client_name="TestClient", created_by=self.user)
        self.project_data = {
            'project_name': 'TestProject',
            'users': [self.user.id]
        }

    def test_create_client(self):
        url = reverse('client-list')  # works only if using DefaultRouter
        data = {'client_name': 'NewClient'}
        response = self.client.post(url, data)
        print(response.data)  # DEBUGGING
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['client_name'], 'NewClient')

    def test_get_all_clients(self):
        url = reverse('client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['data']), 1)

    def test_update_client(self):
        url = reverse('client-detail', args=[self.client_obj.id])
        data = {'client_name': 'UpdatedClient'}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['client_name'], 'UpdatedClient')

    def test_create_project_for_client(self):
        url = reverse('create-project', args=[self.client_obj.id])
        response = self.client.post(url, self.project_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['data']['project_name'], 'TestProject')
        self.assertEqual(response.data['data']['client'], 'TestClient')

    def test_get_projects_for_loggedin_user(self):
        project = Project.objects.create(
            project_name='UserProject',
            client=self.client_obj,
            created_by=self.user
        )
        project.users.add(self.user)
        url = reverse('user-projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'][0]['project_name'], 'UserProject')
