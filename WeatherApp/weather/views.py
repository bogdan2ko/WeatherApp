from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.http import HttpResponse, HttpResponseNotFound, Http404


def index(request):
    appid = "bec8660e4f68fccfd04beece00aacd70"
    url = (
        "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="
        + appid
    )

    if request.method == "POST":
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()[::-1][:1]



    last_object = City.objects.last()
    if last_object:
        last_object.delete()

    all_cities = []
    try:
        for city in cities:
            res = requests.get(url.format(city.name)).json()
            if res.get("main"):
                city_info = {
                    "city": city.name,
                    "temp": res["main"]["temp"],
                    "icon": res["weather"][0]["icon"],
                }
            all_cities.append(city_info)
    except:
        raise Http404()

    context = {"all_info": all_cities, "form": form}

    return render(request, "weather/index.html", context)


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Город не найден</h1>")
