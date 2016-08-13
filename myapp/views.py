from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.request import Request
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
import django_filters
from rest_framework import filters
from .serializers import *
from .models import *
# Create your views here.
class userApiView(generics.ListCreateAPIView):
    queryset = user.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserWriteSerializer
        return UserSerializer

class dataApiView(generics.ListCreateAPIView):
    queryset = data.objects.all()
    def get_serializer_class(self):
        return dataSerializer

class projectApiView(generics.ListCreateAPIView):
    queryset = projects.objects.all()
    def get_serializer_class(self):
        return projectSerializer

