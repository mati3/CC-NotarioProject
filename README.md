# Notario Project:

Vamos a generar una aplicación que haga la finalidad de un notario, para que se puedan consensuar acuerdos, compromisos o contratos por las partes convenientes de los mismos.

En el proyecto nos vamos a basar en una arquitectura basada en microservicios, vamos a intentar implementar varios microservicios, como mínimo dos que interactúen entre si.

Para interactuar entre si, los microservicios usaran colas de eventos, los cuales implementan unos sistemas de comunicación asíncrona de forma que el un servicio pueden decidir a qué mensajes contesta o de qué tipo de eventos van a recibir comunicación.

Cada microservicio se intentará hacer en un lenguaje de programación diferente.

Microservicios:
 - Almacenamiento de log cuando ocurra un evento.
 - Lectura de datos de usuario.
 - Búsqueda de datos en la base de datos y devolución de los que corresponda al usuario.

Usaremos una BBDD Sql para los datos de usuarios y una BBDD NoSql para el contenido de la web.
