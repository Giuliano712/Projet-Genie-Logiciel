from django.db import models

# Create your models here.
class Tache(models.Model):
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
