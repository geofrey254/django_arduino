from rest_framework import serializers
from .models import Serial


class SerialSerializer(serializers.ModelSerializer):
    is_on = serializers.BooleanField()
