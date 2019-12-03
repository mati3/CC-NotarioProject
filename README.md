# Personal Web Project:
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Build Status](https://travis-ci.com/mati3/CC-WebProject.svg?branch=master)](https://travis-ci.com/mati3/CC-WebProject) [![CircleCI](https://circleci.com/gh/mati3/CC-WebProject.svg?style=svg)](https://circleci.com/gh/mati3/CC-WebProject) [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://cc-webproject.herokuapp.com/)  [![codecov](https://codecov.io/gh/mati3/CC-WebProject/branch/master/graph/badge.svg)](https://codecov.io/gh/mati3/CC-WebProject)


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

* Para la integración continua en Ruby, vamos a usar Travis
* Para la integración continua en Python, vamos a usar Circleci.

En ambos lenguajes hemos usado un controlador de versiones, un manejador de dependencias y un módulo de test de alto nivel:

    Lenguaje:   Control versiones:  Manejador dependencias:     Modulo test:

    Ruby        RVM                 Bundler                     Rspec
    Python      Virtualenv          Pip                         Pytest

[Rake](https://github.com/ruby/rake) nos sirve para automatizar la ejecución de comandos, nos proporciona una implementación limpia y de alto nivel. Tendremos que incluir el archivo rakefile:

    buildtool: rakefile

Al igual que con rake en Ruby, [invoke](http://www.pyinvoke.org/) proporciona una API de alto nivel para ejecutar tareas, vamos a usar invoke para definir y organizar nuestras funciones desde un archivo:
    
    buildtool: tasks.py

Enlace a la documentación extendida de la [integración continua](doc/integracion_continua.md) de mi proyecto. 

## Contenedores:

Hemos levantado nuestro microservicio Catalogo, en el cual usamos Ruby.

Hemos desacoplado el modelo del sistema real, elevando a un nivel superior la ejecución de nuestra clase "producto", hemos creado la clase "catalogo" y un fichero de prueba .json que haría de base de datos para probar su funcionalidad. Hemos añadido varias rutas en nuestra api rest, podemos usar las siguientes:

        http://localhost:5000                       # hola mundo
        http://localhost:5000/todos                 # json con todos los productos
        http://localhost:5000/producto/00101        # json con el producto que tiene definido esa ID
        http://localhost:5000/producto/00102
        http://localhost:5000/producto/00103
        http://localhost:5000/producto/00104

Creamos pruebas con [Rack-Test](https://github.com/rack-test/rack-test) para la app creada y como queremos levantar varios servicios web de nuestro microservicio al mismo tiempo. Usamos [foreman](https://github.com/ddollar/foreman) como administrador, este llama al gestor de procesos web rackup, por último lo hemos automatizado incluyéndolo en nuestro archivo Rakefile.

Para levantar cuatro procesos web con foreman:

        foreman start -c web=4

Enlace a la documentación extendida del [microservicio](doc/microservicio.md)

Desplegamos nuestro microservicio en un contenedor Docker, lo subimos al registro de [Docker-Hub](https://hub.docker.com/r/mati3/webproject) y por último lo hemos desplegado el contenedor Docker en [Heroku](https://dashboard.heroku.com/apps/cc-webproject).

Contenedor: https://hub.docker.com/r/mati3/webproject

Enlace a la documentación extendida del [contenedor](doc/contenedores.md) de mi proyecto. 

Podemos probar nuestra aplicación en la web de Heroku con las siguientes rutas:

- [https://cc-webproject.herokuapp.com/](https://cc-webproject.herokuapp.com/)  
- [https://cc-webproject.herokuapp.com/todos](https://cc-webproject.herokuapp.com/todos)
- [https://cc-webproject.herokuapp.com/producto/00101](https://cc-webproject.herokuapp.com/producto/00101)
- [https://cc-webproject.herokuapp.com/producto/00102](https://cc-webproject.herokuapp.com/producto/00102)
- [https://cc-webproject.herokuapp.com/producto/00103](https://cc-webproject.herokuapp.com/producto/00103)
- [https://cc-webproject.herokuapp.com/producto/00104](https://cc-webproject.herokuapp.com/producto/00104)