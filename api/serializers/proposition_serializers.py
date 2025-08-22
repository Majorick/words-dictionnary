from rest_framework import serializer
from api.models import proposition


class PropositionSerializer(serializer.ModelSerializer):
    class Meta:
        model= Proposition
        fields="_all_"