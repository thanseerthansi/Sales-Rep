from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password
from rest_framework import status

from rest_framework import status
from Userapp.serializers import *
from Userapp.models import *
from Salesapp.models import *
from Salesapp.serializers import *
from sales.validation import Validate