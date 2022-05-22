from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serialisation du model utilisateur """
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']



class GroupSerializer(serializers.HyperlinkedModelSerializer):
    """ Serialisation du model group user"""
    class Meta:
        model = Group
        fields = ['url', 'name']