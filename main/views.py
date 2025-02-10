from django.shortcuts import render
import requests
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class CurrentWeatherView(APIView):
    def get(self, request, city_name):
        api_key = "c28cb8878a69422985e102803253101"
        base_url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}&aqi=no"

        response = requests.get(base_url)
        
        if response.status_code == 200:
            data = response.json()
            weather_info = {
                "Shahar nomi": data['location']['region'],
                "Davlat": data['location']['country'],
                "Yangilanish vaqti": data['current']['last_updated'],
                "Havo harorati": f"{data['current']['temp_c']}" + " °C",
                "Shamol tezligi": f"{data['current']['wind_kph']}" + ' km/h', 
            }
            return Response(weather_info, status=status.HTTP_200_OK)
        else:
            return Response({"Error": "Shahar topilmadi yoki noto'g'ri nom kiritildi."}, status=status.HTTP_400_BAD_REQUEST)