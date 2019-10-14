# Notario Project:

Vamos a generar una aplicación que haga la finalidad de un notario, para que se puedan consensuar acuerdos, compromisos o contratos por las partes convenientes de los mismos. Vamos a implementar una serie de contratos, a los cuales un usuario podrá introducir los datos correspondientes y el sistema le ofrecerá los contratos realizados por su persona (una vez identificado).

***Posibles Contratos:***

    Alquiler de un vehículo: fecha inicio, fecha fin, datos vehículo, datos de la parte arrendadora (dueño del vehículo), datos de la parte arrendataria (persona que alquila), precio, clausulas.

    Compraventa de un vehículo: fecha, datos vehículo (ficha técnica), datos de la parte vendedora, datos de la parte compradora, precio, clausulas.

    Alquiler de una vivienda: fecha inicio, fecha fin, datos vivienda, datos de la parte arrendadora (dueño de la vivienda), datos de la parte arrendataria (persona que alquila), precio, clausulas.

    Compraventa de una vivienda: fecha, datos de la vivienda (ubicación), datos de la parte vendedora, datos de la parte compradora, precio, clausulas.

***Datos:***

    Fecha: día/mes/año
    Persona: Nombre, apellidos, dirección, DNI, tipo (arrendador, arrendatario, vendedor, comprador).
    Precio:
    Vivienda: dirección, referencia catastral, descripción.
    Vehículo: Marca, modelo, matriculo, kilómetros, tipo de combustible.
    Clausulas: 
    Login: email y pasword

En el proyecto nos vamos a basar en una arquitectura basada en microservicios, vamos a intentar implementar varios microservicios, como mínimo dos que interactúen entre si.

Para interactuar entre si, los microservicios usaran colas de eventos, los cuales implementan unos sistemas de comunicación asíncrona de forma que el un servicio pueden decidir a qué mensajes contesta o de qué tipo de eventos van a recibir comunicación.

Cada microservicio se intentará hacer en un lenguaje de programación diferente, probablemente usaremos Ruby, TypeScript y si podemos Node.js, usamos Ruby porque queremos avanzar en su aprendizaje y TypeScript porque queremos conocer este lenguaje para usarlo en nuestros proyectos futuros.

Entendemos microservicios como funcionalidades independientes de nuestra aplicación, como pueden ser acceso a perfiles de usuario, catalogo de contratos, login, introducción de datos de cada contrato (formulario), --> muestra a un usuario de los contratos realizados

***Microservicios:***

     - Perfiles de usuario.
     - Catalogo de contratos.
     - Formulario.
     - Inventario de contratos de un usuario.
     - Login.


![imagen](doc/img/Esquema_microservicios.png)

Vamos a implementar "catalogo" e "inventario" como mínimo, e iremos avanzando en funcionalidades dependiendo del buen avance del proyecto.

***Flujo de datos (como se comunican nuestros microservicios):***"login", si el usuario existe en "perfiles", si el contrato existe en "catalogo" devuelve la plantilla, introduce los datos y los guarda en el microservicio "inventario".

Como no vamos a hacer la aplicación completa, solo un par de microservicios, vamos a hacer un archivo json con los datos que se introduce en un contrato para contrastar que se guarda en el usuario correspondiente y los muestra. 

Usaremos una BBDD PostgreSql para los datos implementados en Ruby, y MongoDB para el microservicio implementado en TypeScript.

PostgreSQL es un sistema de gestión de bases de datos relacional orientado a objetos y de código abierto (gratuito y libre) y MongoDB es un sistema de base de datos NoSQL orientado a documentos y también es de código abierto, principal razón para nuestra elección.