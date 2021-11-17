from rest_framework import serializers
from .models import user, Customer


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = '__all__'



class Customer_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'
        depth = 1