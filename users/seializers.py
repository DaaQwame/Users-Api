from calendar import c
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Usersdata

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usersdata
        fields = ['id','name','age','gender','children']