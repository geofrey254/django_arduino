from rest_framework import serializers
from .models import Serial


class SerialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serial
        fields = ['id', 'is_on']
