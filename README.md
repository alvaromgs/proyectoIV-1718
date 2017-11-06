# Proyecto de Infraestructura Virtual 2017-2018
[![Build Status](https://travis-ci.org/alvaromgs/proyectoIV-1718.svg?branch=master)](https://travis-ci.org/alvaromgs/proyectoIV-1718)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/alvaromgs/proyectoIV-1718)

## Descripción

Se pretende realizar la implementación y despliegue de un bot de Telegram que ofrezca al usuario la posibilidad de gestionar listas personalizadas de películas, series o documentales. Las principales funcionalidades que ofrecería serían crear, consultar, modificar o eliminar dichas listas además de contar con un sistema de puntuaciones desde el que se podrá valorar el contenido que ya se haya visualizado.

## Servicios

* pyTelegramBotAPI
* Desarrollo en Python
* PostgreSQL
* Flask

## Despliegue en Heroku

Instalamos el toolbelt de Heroku:

```
sudo add-apt-repository "deb https://cli-assets.heroku.com/branches/stable/apt ./"

curl -L https://cli-assets.heroku.com/apt/release.key | sudo apt-key add -

sudo apt-get update

sudo apt-get install heroku
```

Nos identificamos introduciendo nuestras credenciales de la cuenta de Heroku:

```
heroku login
```

Estando situados en el directorio local del repositorio de nuestro proyecto creamos la aplicación en Heroku especificando la región en la que se alojará y el nombre:

```
heroku create --region eu filmlists
```

Añadimos en la raíz de nuestra aplicación un fichero llamado Procfile cuyo contenido será el comando que necesita Heroku para ponerla en marcha:

```
web: python3 bot/app.py
```

Desplegamos el código de nuestra aplicación:

```
git push heroku master
```

Y ya se encontrará desplegada. Para acceder a ella podremos hacerlo desde la URL que se haya generado o desde el terminal:

```
heroku open
```