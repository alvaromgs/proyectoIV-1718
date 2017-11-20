# Proyecto de Infraestructura Virtual 2017-2018
[![Build Status](https://travis-ci.org/alvaromgs/proyectoIV-1718.svg?branch=master)](https://travis-ci.org/alvaromgs/proyectoIV-1718)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/alvaromgs/proyectoIV-1718)

## Descripción

Se pretende realizar la implementación y despliegue de un bot de Telegram que ofrezca al usuario la posibilidad de gestionar listas personalizadas de películas, series o documentales. Las principales funcionalidades que ofrecería serían crear, consultar, modificar o eliminar dichas listas, además de contar con un sistema de puntuaciones desde el que se podrá valorar el contenido que ya se haya visualizado.

## Servicios

* pyTelegramBotAPI
* Desarrollo en Python
* PostgreSQL
* Flask

## Despliegue en Heroku

Instalamos el *toolbelt* de Heroku:

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

Estando situados en el directorio local del repositorio de nuestro proyecto, creamos la aplicación en Heroku especificando la región en la que se alojará y el nombre:

```
heroku create --region eu filmlists
```

Añadimos en la raíz de nuestra aplicación un fichero llamado **Procfile**, cuyo contenido será el comando que necesita Heroku para ponerla en marcha:

```
web: python3 bot/app.py
```

Por último, configuramos el despliegue automático asociando la aplicación de Heroku con nuestra cuenta de GitHub:

1. En nuestro *dashboard* de Heroku y dentro de la aplicación accedemos a **Deploy**
2. Seleccionamos GitHub como **Deployment method**
3. Conectamos la app en cuestión introduciendo las credenciales de nuestra cuenta de GitHub
4. Indicamos el repositorio de GitHub de nuestra aplicación
5. Activamos los despliegues automáticos para la rama *master* con la opción para que utilice el servicio de integración continua activada pulsando en **Enable Automatic Deploys**

### Rutas definidas en la aplicación

* **/** devuelve el json `{"status":"OK"}`.
* **/listas** devuelve un json con las listas existentes.
* **/lista** devuelve un json con el contenido de la lista solicitada. Requiere parámetro GET (acceder a la ruta para más información).
* **/add** añade una película a la lista indicada. Requiere parámetros GET (acceder a la ruta para más información).

Despliegue https://filmlists.herokuapp.com/

## Despliegue en Docker Hub

Una vez añadido el [Dockerfile](https://github.com/alvaromgs/proyectoIV-1718/blob/master/Dockerfile), creamos un repositorio en Docker Hub y lo sincronizamos con el repositorio de GitHub. Para ello, primero sincronizamos nuestra cuenta de GitHub con Docker Hub en **Settings** > **Linked Accounts & Services** y, posteriormente, indicamos el repositorio donde está alojada nuestra aplicación en **Create** > **Create Automated Build**. Para ejecutar el contenedor desplegado:

```
sudo docker run -p 5000:5000 -it --rm alvaromgs/proyectoiv-1718
```

Para desplegar con Zeit instalamos **now** con:

```
npm install -g now
```

Creamos nuestra cuenta en Zeit con nuestro email y desplegamos el contenedor ejecutando `now` situados en el directorio del proyecto. Obtenemos la URL:

Contenedor https://proyectoiv-1718-rpqvvfszzv.now.sh/

Repositorio en Docker Hub: https://hub.docker.com/r/alvaromgs/proyectoiv-1718/