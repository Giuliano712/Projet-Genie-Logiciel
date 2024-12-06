from django.db import models
from django.contrib.auth.models import User  # Import du modèle utilisateur


# Create your models here.
class Tache(models.Model):
    IMPORTANCE_CHOICES = [
        ('Basse', 'Basse'),
        ('Moyenne', 'Moyenne'),
        ('Haute', 'Haute'),
    ]
    ETAT_CHOICES = [
        ('TO DO', 'TO DO'),
        ('DOING', 'DOING'),
        ('DONE', 'DONE'),
    ]

    titre = models.CharField(max_length=100)
    etat = models.CharField(
        max_length=100,
        choices=ETAT_CHOICES,
        default='TO DO'
    )
    importance = models.CharField(
        max_length=100,
        choices=IMPORTANCE_CHOICES,
        default='Moyenne'
    )
    deadline = models.CharField(max_length=100)
    commentaire = models.TextField(blank=True, null=True)  # Champ pour les commentaires
    utilisateurs = models.ManyToManyField(User, related_name="taches")  # Relation avec les utilisateurs

    def __str__(self):
        return self.titre
