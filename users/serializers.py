from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        user = CustomUser.objects.create(**validated_data)
        return user

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'balance']
