from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings



class Langue(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom