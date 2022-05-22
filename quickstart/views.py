from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User, Group
from .serializers import UserSerializer, GroupSerializer

# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    """ Vue d'affichage et modification des utilisateurs """
    
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]



class GroupViewset(viewsets.ModelViewSet):
    """ Vue d'affichage et modification des utilisateurs """
    
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]