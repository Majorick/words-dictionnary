from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Proposition(models.Model):
    mot = models.ForeignKey("Mot", on_delete=models.CASCADE, related_name="propositions")
    texte_propose = models.CharField(max_length=200)
    definition_propose = models.TextField()
    proposeur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    valide = models.BooleanField(default=False)
    date_proposition = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Proposition pour {self.mot.texte}"