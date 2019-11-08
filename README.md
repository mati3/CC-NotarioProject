# Personal Web Project:
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.com/mati3/CC-WebProject.svg?branch=master)](https://travis-ci.com/mati3/CC-WebProject) [![CircleCI](https://circleci.com/gh/mati3/CC-WebProject.svg?style=svg)](https://circleci.com/gh/mati3/CC-WebProject)

Tenemos como proyecto para una tienda Online, vamos a hacer parte del proyecto personal en esta asignatura, queremos tener un servicio web Restful que proporcione servicio a una futura aplicación con la que los clientes puedan ver los productos ofertados, comprar o visualizar sus compras anteriores y gestionar las ventas de la tienda.

## Arquitectura:

* En el proyecto nos vamos a basar en una arquitectura basada en microservicios, vamos a intentar implementar varios microservicios.

* Enlace a la documentación extendida de la [arquitectura](doc/arquitectura.md).

* Cada microservicio se intentará hacer en un lenguaje de programación diferente, aunque como lenguaje principal vamos a usar Ruby con el Framework [sinatra](http://sinatrarb.com/) para servicios web, es open source, es flexible, sencillo y rápido. 

* Las bases de datos a usar serán MongoDB y PostgreSQL, como usaremos una para cada microservicio, dependerá del lenguaje de programación del mismo.

* Para la gestión de bibliotecas usaremos RubyGems. La cual fue creada especificamente para Ruby, esta biblioteca ayuda a la administración de los diferentes frameworks y bibliotecas. Esto nos lleva a que el desarrollo del proyecto en este lenguaje sea fácil y rápido.

* Sinatra es un framework minimo para el desarrollo web en Ruby, resulta ideal para los servicios web (nuestra Api rest). Es flexible, muy rapido y open source. Enlace a una introducción de uso de [Sinatra](http://sinatrarb.com/intro-es.html).

## Historias de usuario:

* Cualquier usuario  accederá al catalogo de compras, el usuario identificado podrá obtener información de los artículos que haya comprado sólo ingresando su email. Por cada acción del sistema, se guardará el log.

- [Consultar productos.](https://github.com/mati3/CC-WebProject/issues/18) 
- [Realizar una compra.](https://github.com/mati3/CC-WebProject/issues/20)
- [Consultar compras de un usuario.](https://github.com/mati3/CC-WebProject/issues/21)

## Integración continua:

* Para la integración continua en Ruby, vamos a usar Travis.
* Para la integración continua en Python, vamos a usar Circleci.

En ambos lenguajes hemos usado un controlador de versiones, un manejador de dependencias y un módulo de test de alto nivel:

    Lenguaje:   Control versiones:  Manejador dependencias:     Modulo test:

    Ruby        RVM                 Bundler                     Rspec
    Python      Virtualenv          Pip                         Pytest

Con un manejador puedes cambiar entre versiones del lenguaje en tu sistema.
El manejador de dependencias nos provee de un ambiente consistente para nuestros proyectos asegurando que estarán las dependencias que necesitemos para el mismo en un entorno de trabajo aislado del sistema operativo principal.

Después hemos incluido las integraciones continuas con los archivos necesarios para cada una:

    Lenguaje    Integración continua    Archivo

    Ruby        Travis-CI               .travis.yml
    Python      CircleCI                .circleci/config.yml

Ejecución de los test en ruby del proyecto:
buildtool: rake

Enlace a la documentación extendida de la [integración continua](doc/integracion_continua.md) de mi proyecto. 

 Enlace a el badge de Travis: [![Build Status](https://travis-ci.com/mati3/CC-WebProject.svg?branch=master)](https://travis-ci.com/mati3/CC-WebProject)

 Enlace al badge de Circleci: [![CircleCI](https://circleci.com/gh/mati3/CC-WebProject.svg?style=svg)](https://circleci.com/gh/mati3/CC-WebProject)