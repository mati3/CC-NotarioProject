# Personal Web Project:

Tenemos como proyecto para una tienda Online, vamos a hacer parte del proyecto personal en esta asignatura, queremos tener un servicio web Restful que proporcione servicio a una futura aplicación con la que los clientes puedan ver los productos ofertados, comprar o visualizar sus compras anteriores y gestionar las ventas de la tienda.

## Arquitectura:

* En el proyecto nos vamos a basar en una arquitectura basada en microservicios, vamos a intentar implementar varios microservicios, como mínimo dos que interactúen entre si.
[Documentación de Microsoft sobre microservicios y su arquitectura.](https://docs.microsoft.com/es-es/dotnet/architecture/microservices/multi-container-microservice-net-applications/microservice-application-design)

***Microservicios:***

     - Usuarios (gestión de perfiles de usuario).
     - Catalogo (gestión de la base de catalogo de productos).
     - Cesta (muestra los pedidos de un usuario).
 
![imagen](img/Esquema_microservicios.png)

* Las comunicaciones entre microservicios se hará a traves del Gateway, esto se va ha hacer por razones de seguridad, para poder monitorear la Api (si nos diera tiempo).

* La comunicación entre "Gateway" y los microservicios "Catalogo" y "Usuarios" será a través de paso de mensajes con Api Rest, sin embargo la comunicación entre "Gateway" y "Cesta"  vamos a implementar el Bróker de agente de mensajería RabbitMQ, ya que es open source y es compatible con muchos lenguajes. 

* RabbitMQ es un proyecto open source que implementa el estándar AMQP, ademas es compatible con muchos lenguajes (Java, Node.js o Ruby), mensajería de AMQP es un protocolo de comunicación asíncrona a HTTP, esta da al microservicio donde se use, la capacidad de poner en cola las peticiones que le lleguen.

* Configuración distribuida con etcd. Como se comenta en [este](https://www.digitalocean.com/community/tutorials/el-ecosistema-de-docker-descubridor-de-servicio-y-los-almacenes-de-distribucion-de-configuracion-es) articulo, "etcd es una herramienta de descubrimiento de servicio y configuración global distribuida tanto para contenedores como para el sistema host". También se puede usar con [RabbitMQ 3.7.0](https://github.com/rabbitmq/rabbitmq-peer-discovery-etcd) o superior, ademas se puede ejecutar en Ruby facilmente con la instalación de una [gema](https://www.rubydoc.info/gems/etcdv3).

* Cada microservicio se intentará hacer en un lenguaje de programación diferente, aunque como lenguaje principal vamos a usar Ruby con el Framework [sinatra](http://sinatrarb.com/) para servicios web, es open source, es flexible y rápido.

* Para la integración continua vamos a usar [Travis-CI](https://travis-ci.com/).

* Denotar que cada microservicio tendrá su propia base de datos y habrá un servicio general de login del sistema.

* Las bases de datos a usar serán MongoDB y PostgreSQL, como usaremos una para cada microservicio, dependerá del lenguaje de programación del mismo.

* PostgreSQL es un sistema de gestión de bases de datos relacional orientado a objetos y de código abierto (gratuito y libre) y MongoDB es un sistema de base de datos NoSQL orientado a documentos y también es de código abierto, principal razón para nuestra elección.

* Para la gestión de bibliotecas usaremos RubyGems.

* Alojaremos los distintos microservicios de nuestra aplicación en contenedores Docker.

* Haremos un despliegue en la nube, para ello estamos barajando las plataformas Azure ó Amazon.


[Enlace a la siguiente tarea documentada](historias_de_usuario.md)
