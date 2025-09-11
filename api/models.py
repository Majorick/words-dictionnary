from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ("user", "Utilisateur"),
        ("validator", "Validateur"),
        ("admin", "Administrateur"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="user")
    is_validated = models.BooleanField(default=False)  # admin doit valider le compte

    def __str__(self):
        return f"{self.username} ({self.role})"

class Langue(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

 

class Mot(models.Model):
    texte = models.CharField(max_length=2000)
    langue = models.ForeignKey("Langue", on_delete=models.CASCADE, related_name="mots")
    definition = models.TextField()
    auteur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    valide = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.texte} ({self.langue.nom})"


class Proposition(models.Model):
    mot = models.ForeignKey("Mot", on_delete=models.CASCADE, related_name="propositions")
    texte_propose = models.CharField(max_length=200)
    definition_propose = models.TextField()
    proposeur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    valide = models.BooleanField(default=False)
    date_proposition = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Proposition pour {self.mot.texte}"

        