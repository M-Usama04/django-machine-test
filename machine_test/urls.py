"""
URL configuration for machine_test project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token  # ✅ FIXED
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    return Response({
        "message": "Welcome to the Machine Test API",
        "endpoints": [
            "/api/clients/",
            "/api/clients/<id>/",
            "/api/clients/<id>/projects/",
            "/api/projects/",
            "/api-token-auth/"
        ]
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root),
    path('api/', include('core.urls')),
    path('api-token-auth/', obtain_auth_token),  # ✅ Token Auth Working Now
]
