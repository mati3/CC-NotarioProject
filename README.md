# Personal Web Project:
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.com/mati3/CC-WebProject.svg?branch=master)](https://travis-ci.com/mati3/CC-WebProject)

Tenemos como proyecto para una tienda Online, vamos a hacer parte del proyecto personal en esta asignatura, queremos tener un servicio web Restful que proporcione servicio a una futura aplicación con la que los clientes puedan ver los productos ofertados, comprar o visualizar sus compras anteriores y gestionar las ventas de la tienda.

## Arquitectura:

* En el proyecto nos vamos a basar en una arquitectura basada en microservicios, vamos a intentar implementar varios microservicios.

* Enlace a la documentación extendida de la [arquitectura](doc/arquitectura.md) (correspondiente al hito 0).

* Cada microservicio se intentará hacer en un lenguaje de programación diferente, aunque como lenguaje principal vamos a usar Ruby con el Framework [sinatra](http://sinatrarb.com/) para servicios web, es open source, es flexible, sencillo y rápido. 

* Para la [integración continua](doc/integracion_continua.md) vamos a usar [Travis-CI](https://travis-ci.com/). 

* Las bases de datos a usar serán MongoDB y PostgreSQL, como usaremos una para cada microservicio, dependerá del lenguaje de programación del mismo.

* Para la gestión de bibliotecas usaremos RubyGems.

* Alojaremos los distintos microservicios de nuestra aplicación en contenedores Docker.

* Haremos un despliegue en la nube, para ello estamos barajando las plataformas Azure ó Amazon.

## Historias de usuario:

* Cualquier usuario  accederá al catalogo de compras, el usuario identificado podrá obtener información de los artículos que haya comprado sólo ingresando su email. Por cada acción del sistema, se guardará el log.

Enlace a las [Historias de usuario:](https://github.com/mati3/CC-WebProject/milestone/3)

- [Consultar productos.](https://github.com/mati3/CC-WebProject/issues/18) 
- [Consultar usuarios.](https://github.com/mati3/CC-WebProject/issues/19)
- [Realizar una compra.](https://github.com/mati3/CC-WebProject/issues/20)
- [Consultar compras de un usuario.](https://github.com/mati3/CC-WebProject/issues/21)

Enlace a la documentación [integración continua](integracion_continua.md)
