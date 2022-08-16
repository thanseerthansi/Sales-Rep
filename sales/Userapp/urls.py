from django.urls import path


from .views import *

urlpatterns = [
   path('area/',AreaView.as_view()),
   path('route/',RouteView.as_view()),
   path('user/',UserView.as_view()),
   path('login/',LoginView.as_view()),
   path('logout/',Logout.as_view()),
   path('whoami/',WhoAmI.as_view()),
   path('otplogin/',otpLogin.as_view()),
  
   
   
  
]