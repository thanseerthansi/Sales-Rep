# from distutils.command.upload import upload
# from typing_extensions import Self
from django.db import models


from Userapp.models import *

# Create your models here.



# class AttendanceModel(models.Model):
#     staff = models.ForeignKey(UserModel,on_delete=models.CASCADE)
#     punch_in = models.TimeField()
#     punch_out = models.TimeField(null=True)
#     total_time = models.CharField(max_length=100,null=True)
#     description = models.TextField(null=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)

class ProductModel(models.Model):
    
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Image',blank=True,null=True)
    price = models.FloatField(default=0.0)
    stock = models.FloatField(default=0.0)
    have_subproduct = models.BooleanField(default=False)
    description =models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class SubproductModel(models.Model):
    product = models.ForeignKey(ProductModel,on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Image',blank=True,null=True)
    price = models.FloatField(default=0.0)
    stock = models.FloatField(default=0.0)
    description = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class OrderModel(models.Model):
    customer = models.ForeignKey(UserModel,on_delete=models.CASCADE,related_name='customer')
    employee  = models.ForeignKey(UserModel,on_delete=models.DO_NOTHING,null=True,related_name='employee')
    # orders= models.ManyToManyField(SubproductModel)
    total_price = models.FloatField(default=0.0)
    description = models.TextField(null=True,blank=True)
    is_paid = models.BooleanField(default = False)
    is_delivered = models.BooleanField(default = False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class OrderedProductModel(models.Model):
    order_id = models.ForeignKey(OrderModel,on_delete=models.CASCADE)
    product = models.CharField(max_length=100,null=True)
    product_id = models.IntegerField(null=True,blank=True,default=None)
    subproduct_id = models.IntegerField(null=True,blank=True)
    product_price = models.FloatField(default=0.0)
    quantity = models.FloatField(default=0.0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

