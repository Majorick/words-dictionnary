from rest_framework import serializer
from api.models import Langue


class LangueSerializer(serializer.ModelSerializer):
    class Meta:
        model= Langue
        fields="_all_"