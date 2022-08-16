# from tkinter import CASCADE
# from time import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
# from Salesapp.models import AreaModel


# Create your models here.



class RouteModel(models.Model):
    route = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True,null=True)
    updated_date  = models.DateField(auto_now=True,null=True)

class AreaModel(models.Model):
    area_name = models.CharField(max_length=100,null=True)
    route = models.ForeignKey(RouteModel,on_delete=models.CASCADE)
    description = models.TextField(null=True,blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class UserModel(AbstractUser):
    photo = models.ImageField(upload_to='Image',blank=True,null=True)
    is_employee = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    route = models.ForeignKey(RouteModel,on_delete=models.CASCADE,null=True,blank=True)
    address = models.TextField(null=True)
    area = models.ForeignKey(AreaModel,on_delete=models.CASCADE,null=True)
    contact = models.CharField(max_length=100,null=True)
    longitude = models.CharField(max_length=100,null=True,blank=True)
    latitude = models.CharField(max_length=100,null=True,blank=True)

# class Otp(models.Model):
#   user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
#   otp = models.IntegerField()
#   created_on = models.DateTimeField(default=timezone.now())

#   class Meta:
#     db_table = "otp"
    