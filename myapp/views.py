from rest_framework.views import APIView
from django.http import *
from django.template import *
from django.shortcuts import *
import json
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
        if(UserSerializer.count==1):
            return UserSerializer
        else:
            return 1

def login(request):
    if(request.method=='POST'):
        Array = json.loads(request.body)
        count=user.objects.filter(username=Array['username'],password=Array['password']).count()
        if(count==1):
            user1=user.objects.get(username=Array['username'],password=Array['password'])
            request.session['username']=Array['username']
            response = {}
            response['status'] = 0
            return HttpResponse(json.dumps(response))
        else:
            response={}
            response['status']=1
            return HttpResponse(json.dumps(response))
    else:
        return render(request,'myapp/login.html')

class dataApiView(generics.ListCreateAPIView):
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('state')
    def get_queryset(self):
        queryset = data.objects.all()
        state = self.request.query_params.get('state', None)
        if state is not None:
            queryset = queryset.filter(state=state)
        return queryset

    def get_serializer_class(self):
        return dataSerializer

class projectApiView(generics.ListCreateAPIView):
    queryset=projects.objects.all()
    def get_serializer_class(self):
        return dataSerializer


def indexApiView(request):
    return render(request, 'myapp/index.html')
