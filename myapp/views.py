from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.request import Request

# Create your views here.
class userApiView(generics.ListCreateAPIView):
    queryset = ResidentialComplex.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return UserWriteSerializer
        return UserSerializer