from django.shortcuts import render 
from rest_framework import viewsets, permissions
from .models import Langue, Mot, Proposition
from .serializers import LangueSerializer, MotSerializer, PropositionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAdminUser
from .permissions import IsValidatorOrAdmin


class LangueViewSet(viewsets.ModelViewSet):
    queryset = Langue.objects.all()
    serializer_class = LangueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class MotViewSet(viewsets.ModelViewSet):
    queryset = Mot.objects.filter(valide=True)  # on ne montre que les mots validés au public
    serializer_class = MotSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(auteur=self.request.user, valide=False)  # mot proposé par défaut non validé


class PropositionViewSet(viewsets.ModelViewSet):
    queryset = Proposition.objects.all()
    serializer_class = PropositionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(proposeur=self.request.user, valide=False)


class MotAdminViewSet(viewsets.ModelViewSet):
    queryset = Mot.objects.all()  # Inclut tous les mots, validés ou non
    serializer_class = MotSerializer
    permission_classes = [IsAdminUser]  # seuls les admin/validateurs y ont accès

   

class MotAdminViewSet(viewsets.ModelViewSet):
    queryset = Mot.objects.all()
    serializer_class = MotSerializer
    permission_classes = [IsValidatorOrAdmin]
