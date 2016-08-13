from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields=['username','password']

class UserWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['username','password']

class dataSerializer(serializers.ModelSerializer):
    class Meta:
        model = data
        fields = ['type','area','title','description','date','state','district','for_whom']

class projectSerializer(serializers.ModelSerializer):
    class Meta:
        model = data
        fields = ['title','description','deadline','for_whom']
