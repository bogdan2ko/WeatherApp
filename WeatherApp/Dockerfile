FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1




WORKDIR D:\project2\WeatherApp



RUN pip install --upgrade pip
RUN pip install requests

COPY . . 

RUN pip install --no-cache-dir -r requirements.txt




CMD python manage.py runserver 0.0.0.0:8000