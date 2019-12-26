# Personal Web Project:
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.com/mati3/CC-WebProject.svg?branch=master)](https://travis-ci.com/mati3/CC-WebProject) [![CircleCI](https://circleci.com/gh/mati3/CC-WebProject.svg?style=svg)](https://circleci.com/gh/mati3/CC-WebProject) [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://cc-webproject.herokuapp.com/)  [![codecov](https://codecov.io/gh/mati3/CC-WebProject/branch/master/graph/badge.svg)](https://codecov.io/gh/mati3/CC-WebProject)


Queremos tener un servicio web Restful que proporcione servicio a una futura aplicación con la que los clientes puedan ver los productos ofertados, comprar o visualizar sus compras anteriores y gestionar las ventas de la tienda.

## Arquitectura:

* En el proyecto nos vamos a basar en una arquitectura basada en microservicios, vamos a intentar implementar varios microservicios.

* Enlace a la documentación extendida de la [arquitectura](doc/arquitectura.md).

## Integración continua:

* Para la integración continua en Ruby, vamos a usar Travis
* Para la integración continua en Python, vamos a usar Circleci.

Automatizar la ejecución:

    buildtool: Catalogo/Rakefile         # Rake para Ruby 
    buildtool: Cesta/tasks.py         # Invoke para Python

Enlace a la documentación extendida de la [integración continua](doc/integracion_continua.md) de mi proyecto. 

## Contenedores:

Hemos levantado nuestro microservicio Catalogo, en el cual usamos Ruby.
Usamos [foreman](https://github.com/ddollar/foreman) como administrador, este llama al gestor de procesos web rackup, por último lo hemos automatizado incluyéndolo en nuestro archivo Rakefile.

Para levantar procesos web:

        rake foreman env={numero de procesos}

Enlace a la documentación extendida del [microservicio Catalogo](doc/microservicioCatalogo.md)

Desplegamos nuestro microservicio en un contenedor Docker, lo subimos al registro de [Docker-Hub](https://hub.docker.com/r/mati3/webproject) y por último lo hemos desplegado el contenedor Docker en [Heroku](https://dashboard.heroku.com/apps/cc-webproject).

- Contenedor: https://hub.docker.com/r/mati3/webproject

Enlace a la documentación extendida del [contenedor](doc/contenedores.md) de mi proyecto. 

## Medición de prestaciones:

Prestaciones: Cesta/taurus.yml

En esta tarea se pedía levantar el resto de microservicios, así que levantamos por completo nuestro microservicio "Cesta", realizado en Python y Flask.

Enlace a la documentación extendida del [microservicio Cesta](doc/microservicioCesta.md)

Hemos medido las prestaciones del microservicio nombrado con [Taurus](https://gettaurus.org/). Se estimaba como buen rendimiento unas 1000 peticiones/s  con 10 usuarios concurrentes. Después de algunos ajustes se ha alcanzado la meta propuesta.

Enlace a la documentación extendida de la [medición de prestaciones](doc/taurusCesta.md)