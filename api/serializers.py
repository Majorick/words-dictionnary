from rest_framework import serializers
from .models import Langue, Mot, Proposition
from rest_framework.permissions import BasePermission

class LangueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Langue
        fields = "__all__"

class MotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mot
        fields = "__all__"
        read_only_fields = ["auteur", "valide"]

class PropositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proposition
        fields = "__all__"
        read_only_fields = ["proposeur", "valide"]


from rest_framework.permissions import BasePermission


