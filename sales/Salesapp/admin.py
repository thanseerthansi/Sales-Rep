from django.contrib import admin

from Salesapp.models import *

# Register your models here.

# admin.site.register(AttendanceModel)
admin.site.register(ProductModel)
admin.site.register(SubproductModel)
admin.site.register(OrderModel)
admin.site.register(OrderedProductModel)