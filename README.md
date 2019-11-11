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

Con la integración continua, la combinación de los cambios de código de diferentes equipos de trabajo (supuesto que cada trabajador desarrolla un microservicio diferente), supone la localización y corrección de los errores con rápidez.

Con la integración continua mejoramos la productividad gracias al ahorro de las tareas manuales y la reducción de errores.

* Para la integración continua en Ruby, vamos a usar Travis: [![Build Status](https://travis-ci.com/mati3/CC-WebProject.svg?branch=master)](https://travis-ci.com/mati3/CC-WebProject)
* Para la integración continua en Python, vamos a usar Circleci: [![CircleCI](https://circleci.com/gh/mati3/CC-WebProject.svg?style=svg)](https://circleci.com/gh/mati3/CC-WebProject)

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


[Rake](https://github.com/ruby/rake) nos sirve para automatizar la ejecución de comandos, nos proporciona una implementación limpia y de alto nivel. Tendremos que incluir el archivo rakefile:

    buildtool: rakefile

Al igual que con rake en Ruby, [invoke](http://www.pyinvoke.org/) proporciona una API de alto nivel para ejecutar tareas, vamos a usar invoke para definir y organizar nuestras funciones desde un archivo:
    
    buildtool: tasks.py

Los test avisaran si los cambios efectuados en nuestro código altera el funcionamiento esperado por el microservicio.

Hacemos la integración en local para nuevas invorporaciones con dos script:

    Lenguaje    Integración local (archivo)

    Ruby         new_local_ruby.sh              
    Python       new_local_python.sh 

Por último vamos al archivo gitignore y le diremos los archivos y directorios que queremos no suba al repositorio. Así evitamos enviar código privado, archivos binarios del control de versiones, instalaciones, etc.

Enlace a la documentación extendida de la [integración continua](doc/integracion_continua.md) de mi proyecto. 

