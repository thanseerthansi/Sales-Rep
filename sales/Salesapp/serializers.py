from rest_framework import serializers
from .models import *




class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaModel
        fields = '__all__'

# class AttendanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AttendanceModel
#         fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

class SubproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubproductModel
        fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = '__all__'

class OrderproductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProductModel
        fields = '__all__'