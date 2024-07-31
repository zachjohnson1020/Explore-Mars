from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
import dotenv 


# Create your views here.

def marshome(request):

    #api instance with developer key
    ApodApi= requests.get('https://api.nasa.gov/planetary/apod?api_key=' + os.environ['API_KEY'])
    ApodData = ApodApi.json()
    weatherData = requests.get('https://mars.nasa.gov/rss/api/?feed=weather&category=msl&feedtype=json').json()
    N = 7
    weather = weatherData['soles'][:N]
    roverApi= requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date=2023-10-10&camera=NAVCAM&api_key=' + os.environ['API_KEY'])
    roverData = roverApi.json()

    context = {
        'weather': weather,
        'Apod': ApodData,
        'photos': roverData['photos'],
    }





    return render( request,"marshome.html", context)