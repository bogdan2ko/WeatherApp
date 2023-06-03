from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.core.cache import cache

def index(request):
    appid = "bec8660e4f68fccfd04beece00aacd70"
    url = (
        "https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="
        + appid
    )

    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            # Получаем название города из формы
            city_name = form.cleaned_data['name']
            # Создаем объект города и сохраняем его в базе данных
            city = City.objects.create(name=city_name)
            # Очищаем кэш данных, чтобы обновить информацию
            cache.delete('weather_data')

    form = CityForm()

    # Получаем все города из базы данных
    cities = City.objects.all()[::-1][:1]

    # Если в кэше есть данные, получаем их
    cached_data = cache.get('weather_data')
    if cached_data:
        all_cities = cached_data
    else:
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
            # Кэшируем данные на 10 секунд
            cache.set('weather_data', all_cities, 10)
        except:
            raise Http404()

    context = {"all_info": all_cities, "form": form}

    return render(request, "weather/index.html", context)



def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Город не найден</h1>")
