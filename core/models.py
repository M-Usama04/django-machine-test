from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    """
    Represents a client (organization or customer).
    A client can have many projects.
    """
    client_name = models.CharField(max_length=255, unique=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='clients_created',
        help_text="User who created this client"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.client_name

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Project(models.Model):
    """
    Represents a project under a client.
    A project can be assigned to multiple users.
    """
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='projects',
        help_text="Client this project belongs to"
    )
    users = models.ManyToManyField(
        User,
        related_name='projects_assigned',
        blank=True,
        help_text="Users assigned to this project"
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects_created',
        help_text="User who created this project"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project_name} ({self.client.client_name})"

    class Meta:
        ordering = ['-created_at']
        unique_together = ('project_name', 'client')  # One project name per client
        verbose_name = "Project"
        verbose_name_plural = "Projects"
