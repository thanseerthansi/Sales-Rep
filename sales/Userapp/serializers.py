from dataclasses import fields
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteModel
        fields = '__all__'
class otpLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["contact"]

