from django.db import models
from users.models import CustomUser

import uuid

# Create your models here.
class Task(models.Model):
    IMPORTANCE_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]
    STATUS_CHOICES = [
        ('TO_DO', 'TO DO'),
        ('DOING', 'DOING'),
        ('DONE', 'DONE'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()

    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='TO_DO')
    importance = models.CharField(max_length=100, choices=IMPORTANCE_CHOICES, default='Medium')
    deadline = models.DateField()
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='tasks')  # Link to a project
    assigned_users = models.ManyToManyField(CustomUser, related_name='tasks')  # Assignable to multiple users

    def __str__(self):
        return self.title


class ClientCompany(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    project_list = models.ManyToManyField('Project', related_name='companies')

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    user_list = models.ManyToManyField(CustomUser, related_name='projects')

    def __str__(self):
        return self.name