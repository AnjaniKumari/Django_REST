from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
# Create your views here.
@api_view(["POST"])
def IdealWeight(fahrenheit_data):
    try:
        fahrenheit=json.loads(fahrenheit_data.body)
        celsius=str(((56*fahrenheit-32)*5)/9)
        return JsonResponse("Converting the value in celsius: "+celsius+"°C",safe=False)
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)