from django.shortcuts import render
from rest_framework import viewsets
from .seializers import UserSerializer
from .models import Usersdata
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = Usersdata.objects.all()
    serializer_class = UserSerializer
