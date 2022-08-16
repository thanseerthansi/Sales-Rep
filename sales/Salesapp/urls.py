from django.urls import path
from .views import *

urlpatterns = [
  
   
   path('product/',ProductView.as_view()),
   path('subproduct/',SubproductView.as_view()),
   path('order/',OrderView.as_view()),
   path('orderproduct/',OrderedproductView.as_view()),
  
]