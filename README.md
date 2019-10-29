# Personal Web Project:
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.com/mati3/CC-WebProject.svg?branch=master)](https://travis-ci.com/mati3/CC-WebProject)

Tenemos como proyecto para una tienda Online, vamos a hacer parte del proyecto personal en esta asignatura, queremos tener un servicio web Restful que proporcione servicio a una futura aplicación con la que los clientes puedan ver los productos ofertados, comprar o visualizar sus compras anteriores y gestionar las ventas de la tienda.

## Arquitectura:

* En el proyecto nos vamos a basar en una arquitectura basada en microservicios, vamos a intentar implementar varios microservicios.

* Enlace a la documentación extendida de la [arquitectura](doc/arquitectura.md) (correspondiente al hito 0).

* Cada microservicio se intentará hacer en un lenguaje de programación diferente, aunque como lenguaje principal vamos a usar Ruby con el Framework [sinatra](http://sinatrarb.com/) para servicios web, es open source, es flexible, sencillo y rápido. 

* Para la [integración continua](doc/integracion_continua.md) vamos a usar [Travis-CI](https://travis-ci.com/). 

* Las bases de datos a usar serán MongoDB y PostgreSQL, como usaremos una para cada microservicio, dependerá del lenguaje de programación del mismo.

* Para la gestión de bibliotecas usaremos RubyGems. La cual fue creada especificamente para Ruby, esta biblioteca ayuda a la administración de los diferentes frameworks y bibliotecas. Esto nos lleva a que el desarrollo del proyecto en este lenguaje sea fácil y rápido.

* Ruby dispone de una gran cantidad de recursos, con muchas bibliotecas disponibles que dan cracterísticas a nuestras aplicaciones web, como la que hemos elegido RubyGems. Además de una amplia documentación oficial y recursos online.

* Tiene una gran comunidad, muy activa y comprometida. Como ellos mismos dicen "[Ruby es el mejor amigo de un desarrollador]()https://www.ruby-lang.org/es/about/".

* Ruby es un lenguaje dinamico orientado a objetos, de propósito general, por lo que sirve para todo tipo de proyectos, así que creemos que con ruby bamos a obtener un entorno cómodo.

* Sinatra es un framework minimo para el desarrollo web en Ruby, resulta ideal para los servicios web (nuestra Api rest). Es flexible, muy rapido y open source. Enlace a una introducción de uso de [Sinatra](http://sinatrarb.com/intro-es.html).

## Historias de usuario:

* Cualquier usuario  accederá al catalogo de compras, el usuario identificado podrá obtener información de los artículos que haya comprado sólo ingresando su email. Por cada acción del sistema, se guardará el log.

Enlace a las [Historias de usuario:](https://github.com/mati3/CC-WebProject/milestone/3)

- [Consultar productos.](https://github.com/mati3/CC-WebProject/issues/18) 
- [Realizar una compra.](https://github.com/mati3/CC-WebProject/issues/20)
- [Consultar compras de un usuario.](https://github.com/mati3/CC-WebProject/issues/21)

