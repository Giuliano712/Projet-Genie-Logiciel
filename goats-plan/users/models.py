from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# Custom User
class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('project_manager', 'Project Manager'),
        ('developer', 'Developer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='developer') #NB: admin will thus be set a dev

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def get_projects(self):
        return self.projects.all()

    def __str__(self):
        return self.username