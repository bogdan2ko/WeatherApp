from django.contrib import admin
from django.urls import path, include
from weather.views import pageNotFound

urlpatterns = [
    path("admin/", admin.site.urls), 
    path("", include("weather.urls"))
    ]

handler404 = pageNotFound
