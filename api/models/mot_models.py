from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Mot(models.Model):
    texte = models.CharField(max_length=200)
    langue = models.ForeignKey("Langue", on_delete=models.CASCADE, related_name="mots")
    definition = models.TextField()
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    valide = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.texte} ({self.langue.nom})"


