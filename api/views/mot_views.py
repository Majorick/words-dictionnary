from django.shortcuts import render 
from rest_framework import viewsets, permissions
from .models import Langue, Mot, Proposition
from .serializers import LangueSerializer, MotSerializer, PropositionSerializer


class MotViewSet(viewsets.ModelViewSet):
    queryset = Mot.objects.filter(valide=True)  # on ne montre que les mots validés au public
    serializer_class = MotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(auteur=self.request.user, valide=False)  # mot proposé par défaut non validé
