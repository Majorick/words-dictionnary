from django.shortcuts import render 
from rest_framework import viewsets, permissions
from .models import Langue, Mot, Proposition
from .serializers import LangueSerializer, MotSerializer, PropositionSerializer



class PropositionViewSet(viewsets.ModelViewSet):
    queryset = Proposition.objects.all()
    serializer_class = PropositionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(proposeur=self.request.user, valide=False)

    def perform_create(self, serializer):