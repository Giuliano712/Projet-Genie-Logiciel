from django.db import models
from users.models import CustomUser

import uuid

# Create your models here.
class Tache(models.Model):  #TODO: make this better with links to projects and users who can see and modify. Try to figure out how to do that
    IMPORTANCE_CHOICES = [
        ('Basse', 'Basse'),
        ('Moyenne', 'Moyenne'),
        ('Haute', 'Haute'),
    ]
    ETAT_CHOICES = [
        ('TO DO','TO DO'),
        ('DOING','DOING'),
        ('DONE','DONE'),
    ]
    titre = models.CharField(max_length=100)
    etat = models.CharField(
        max_length=100,
        choices=ETAT_CHOICES,
        default='TO DO')

    importance = models.CharField(
        max_length=100,
        choices=IMPORTANCE_CHOICES,
        default='Moyenne'
    )
    deadline = models.CharField(max_length=100)

    def __str__(self):
        return self.titre


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