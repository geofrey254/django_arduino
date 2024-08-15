from django.shortcuts import render
from .models import Serial
from .serializers import SerialSerializer
from rest_framework import generics

# Create your views here.


class SerialView(generics.ListCreateAPIView):
    queryset = Serial.objects.all()
    serializer_class = SerialSerializer
