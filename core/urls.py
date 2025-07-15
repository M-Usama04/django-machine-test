# core/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, ProjectCreateView, UserProjectsView

router = DefaultRouter()
router.register('clients', ClientViewSet, basename='client')

urlpatterns = [
    path('', include(router.urls)),
    path('clients/<int:pk>/projects/', ProjectCreateView.as_view(), name='create-project'),
    path('projects/', UserProjectsView.as_view(), name='user-projects'),
]
