from rest_framework import serializer
from api.models import Mot



class MotSerializer(serializer.ModelSerializer):
    class Meta:
        model= Mot
        fields="_all_"
