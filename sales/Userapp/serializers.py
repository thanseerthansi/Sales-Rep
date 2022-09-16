from dataclasses import fields
from rest_framework import serializers
from .models import *





class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteModel
        fields = '__all__'

class AreaSerializer(serializers.ModelSerializer):
    route = serializers.SerializerMethodField()
    class Meta:
        model = AreaModel
        fields = '__all__'
    def get_route(self,obj):
        if obj.route:
            v_obj = RouteModel.objects.filter(id=obj.route.id)
            v_qs = RouteSerializer(v_obj, many=True)
            return v_qs.data
        else:pass

class UserSerializer(serializers.ModelSerializer):
    route = serializers.SerializerMethodField()
    area = serializers.SerializerMethodField()
    class Meta:
        model = UserModel
        fields = '__all__'

    def get_route(self,obj):
        if obj.route:
            v_obj = RouteModel.objects.filter(id=obj.route.id)
            v_qs = RouteSerializer(v_obj, many=True)
            return v_qs.data
        else:pass

    def get_area(self,obj):
        if obj.area:
            v_obj = AreaModel.objects.filter(id=obj.area.id)
            v_qs = AreaSerializer(v_obj , many=True)
            return v_qs.data
        else:pass

class otpLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["contact"]

