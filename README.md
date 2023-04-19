#   WeatherApp

Weather apps enable users to get instant alerts regarding weather conditions. Weather apps are the simplest method to know about the updates of the upcoming weather.

##  Requirements and Preparation

The system requires Docker and Docker Compose for development. It is recommended to use GNU/Linux operating system (Debian, Ubuntu, etc.).

You can configure databse settings in env.dev and in docker-compose.

##  Installation

1. Open the command prompt.
2. Run `docker-compose up -d`
3. You are great, and can start working.

##  Commands

* `docker-compose build` — Creating an image.
* `docker-compose up -d` — Сontainer launch.
* `make init` — Initialize development environment.
* `make up` — Start development environment.
* `make down` — Stop development environment.
* `make makemigrations` — Create new migrations.
* `make migrate` — Apply migrations.
* `make runtests` — Run tests
