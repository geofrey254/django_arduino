from django.shortcuts import render
from .models import Serial
from .serializers import SerialSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

# Create your views here.

@api_view(['GET', 'POST'])
def switcherView(request):
    if request.method == 'GET':  
        # retrieve current switch state from ESP8266
        try: 
            esp_switch = 'https://192.168.1.100'
            response = requests.get(esp_switch)
            return Response(response)
        except requests.exceptions.RequestException as e:
            return Response({"error": str(e)}, status=500)
        
    
    elif request.method == 'POST':
        is_on = request.data.get('is_on')
        #send state to ESP8266
        esp_switch = 'https://192.168.1.100'
        payload = {'is_on' : is_on}
        response = requests.post(esp_switch, json=payload)

        return Response({'is_on': is_on})


