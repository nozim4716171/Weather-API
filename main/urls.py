from django.urls import path
from .views import CurrentWeatherView


urlpatterns = [
    path('current-weather/<str:city_name>/', CurrentWeatherView.as_view(), name='current_weather')
]