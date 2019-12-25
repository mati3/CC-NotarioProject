# Microservicio Cesta:

Microservicio en el lenguaje Python. Elegimos el framework [Flask](https://flask.palletsprojects.com/en/1.1.x/).

Flask es simple, flexible y te da un gran control sobre tu aplicación web, tiene la ventaja de ser poco pesado por lo que consumirá menos recursos, por todo ello encaja perfectamente con el principio de responsabilidad única en la arquitectura basada en microservicios.

Añadimos Flask a nuestro archivo requirements.txt y lo volvemos a ejecutar, recordemos:
    source entorno/bin/activate
    pip3 install -r requirements.txt 

Como de costumbre vamos a levantar una api rest con un mensaje de "hola mundo" para asegurar esta parte. Creamos un archivo "app_Cesta" con el siguiente contenido:

        from flask import Flask
        app = Flask(__name__)


        @app.route('/')
        def hello_world():
            return 'Hello, World!'

        if __name__ == '__main__':
            app.run()

Por defecto se levanta en el puerto 5000, podemos probar que funciona con la orden "python appCesta.py".

Manejador de procesos web [gunicorn](https://gunicorn.org/) cumple la especificación WSGI (Web Server Gateway Interface), es un estándar de Python que describe como se comunica un servidor web con una aplicación web para evitar problemas en la comunicación de las mismas.

Como antes añadimos gunicorn a nuestro archivo requirements.txt

También añadimos la nueva funcionalidad a nuestro archivo tasks.py quedando la tarea automatizada:

    @task
    def start(c):
        c.run("gunicorn -w 5 appCesta:app")

Por defecto puerto 8000, nosotros levantamos 5 en este ejemplo. 

Ejemplo de uso: invoke start

Ya tenemos el entorno en local preparado así que vamos a añadir mongodb (base de datos no relacional) con la librería pymongo.

[Mongodb](https://docs.mongodb.com/) es una base de datos NoSQL, distribuida y escalable horizontalmente. Sus consultas son más rápidas. Datos no estructurados guardados en formato JSON, con un esquema dinámico, alta consistencia, disponibilidad y tolerancia al particionado y no requiere interrupción.

[Instalamos](https://docs.mongodb.com/v3.6/installation/) Mongodb desde el entorno virtualenv: sudo apt install mongodb -y

Iniciamos Mongodb: mongo

Para ver el contenido de la base de datos desde su terminal:

        use baseDeDatos
        db.Clientes.find()
        db.dropDatabase()

Exportar e importar nuestra base de datos a un archivo json, para respaldo y pruebas de la base de datos (tenemos un archivo inicial "CC-WebProject/Cesta/src/client.json"):

    mongoimport --db=baseDeDatos --collection=Clientes --file=client.json
    mongoexport --db=baseDeDatos --collection=Clientes --out=client.json


Posteriormente hemos desacoplado el modelo del sistema real, elevando a un nivel superior la ejecución de nuestras clases y base de datos, hemos creado la clase "catalogo" que gestiona la información que necesitamos de ese microservicio. Hemos generado las clases "cestacliente" que gestiona la información de un cliente y "dbclientes" que sería la clase que gestiona la base de datos y devuelve la información  que necesita nuestra api rest.  Hemos añadido varias rutas, podemos usar las siguientes:

    http://localhost:8000/      # devuelve un "Hola Mundo".
    http://localhost:8000/cesta/{correo}    # devuelve la cesta de un cliente dado su correo.
    http://localhost:8000/clientes  # devuelve todos los clientes existente.
    http://localhost:8000/todo  # devuelve los clientes con sus cestas.
    http://localhost:8000/newclient/{correo} # ingresa un nuevo cliente a la BBDD.
    http://localhost:8000/newcesta/{correo}/{id_producto} # ingresa una nueva cesta a un cliente dado.

Generamos los [test](https://flask.palletsprojects.com/en/1.1.x/testing/) pertinentes para todo el código nuevo, en esta ocasión, para una mejor organización se ha puesto e el nombre de cada test la referencia de la clase a la que se refiere.


