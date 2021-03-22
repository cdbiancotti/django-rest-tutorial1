from django.contrib.auth.models import Group, Permission, User
from rest_framework.decorators import permission_classes
from quickstart.serializers import UserSerializer
from rest_framework import viewsets, permissions
from .serializers import GroupsSerializer, UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupsSerializer
    permission_classes = [permissions.IsAuthenticated]
