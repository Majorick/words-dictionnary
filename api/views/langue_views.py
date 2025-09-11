from django.shortcuts import render 
from rest_framework import viewsets, permissions
from .models import Langue, Mot, Proposition
from .serializers import LangueSerializer, MotSerializer, PropositionSerializer



class LangueViewSet(viewsets.ModelViewSet):
    queryset = Langue.objects.all()
    serializer_class = LangueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        serializer.save(created_by=self.request.user)