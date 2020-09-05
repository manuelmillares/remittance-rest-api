from rest_framework import viewsets
from apps.user import serializers
from apps.core import models


class UserViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
