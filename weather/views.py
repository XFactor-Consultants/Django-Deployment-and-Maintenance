from django.shortcuts import render
from django.conf import settings
import requests
import logging

logger = logging.getLogger('weather.file')


def index(request):
    location = "New%20York"
    logger.warning("Debug message!")
    if 'location' in request.GET:
        location = request.GET["location"]
    r = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+location+"&units=imperial&appid="+settings.OWM_API)
    data = r.json()
    return render(request, 'index.html', {'data': data})
