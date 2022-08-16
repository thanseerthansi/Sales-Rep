from django.contrib import admin

from Userapp.models import AreaModel, RouteModel, UserModel

# Register your models here.

admin.site.register(AreaModel)
admin.site.register(UserModel)
admin.site.register(RouteModel) 