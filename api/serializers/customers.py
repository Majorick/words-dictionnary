from rest_framework import serializer
from api.models import Customers 


class CustomersSerializer(serializer.ModelSerializer):
    class Meta:
        model= Customers
        fields="_all_"