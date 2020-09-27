from rest_framework import viewsets
from apps.remittance import serializers
from apps.core import models
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class RemittanceViewSet(viewsets.ModelViewSet):
    """Handle creating and updating remittances"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.RemittanceSerializer
    queryset = models.Remittance.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return models.Remittance.objects.all()
        return models.Remittance.objects.filter(distributor=self.request.user)
