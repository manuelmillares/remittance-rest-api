from rest_framework import serializers
from apps.core import models


class RemittanceSerializer(serializers.ModelSerializer):
    """Serializer for the remittance object"""

    class Meta:
        model = models.Remittance
        fields = '__all__'
