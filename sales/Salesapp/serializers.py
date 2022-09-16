from rest_framework import serializers

from Userapp.serializers import UserSerializer
from .models import *






# class AttendanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AttendanceModel
#         fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'

class SubproductSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()
    class Meta:
        model = SubproductModel
        fields = '__all__'
    def get_product(self,obj):
        if obj.product:
            v_obj = ProductModel.objects.filter(id=obj.product.id)
            v_qs = ProductSerializer(v_obj, many=True)
            return v_qs.data
        else:pass
        
class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.SerializerMethodField()
    employee = serializers.SerializerMethodField()
    class Meta:
        model = OrderModel
        fields = '__all__'

    def get_customer(self,obj):
        if obj.customer:
            v_obj = UserModel.objects.filter(id=obj.customer.id)
            v_qs = UserSerializer(v_obj, many=True)
            return v_qs.data
        else:pass

    def get_employee(self,obj):
        if obj.employee:
            v_obj = UserModel.objects.filter(id=obj.employee.id)
            v_qs = UserSerializer(v_obj, many=True)
            return v_qs.data
        else:pass

class OrderproductSerializer(serializers.ModelSerializer):
    order_id = serializers.SerializerMethodField()
    class Meta:
        model = OrderedProductModel
        fields = '__all__'
    def get_order_id(self,obj):
        if obj.order_id:
            v_obj = OrderModel.objects.filter(id=obj.order_id.id)
            v_qs = OrderSerializer(v_obj,many=True)
            return v_qs.data
        else:pass