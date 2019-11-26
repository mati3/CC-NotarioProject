#Contenedores

Ya tenemos docker instalado, dejamos el archivo de ejecución para su instalación, lo ejecutamos con "Ansible".

            - name: Install prerequisites docker 
              apt:    
               update_cache: yes
              with_items:
               - apt-transport-https
               - ca-certificates
               - curl
               - software-properties-common

            - name: Add Docker GPG key
              apt_key: 
                url: https://download.docker.com/linux/ubuntu/gpg

            - name: Verify that we have the key with the fingerprint
              apt_key:
                id: 0EBFCD88
                state: present

            - name: Add Docker APT repository
              apt_repository:
                repo: deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable
                update_cache: yes

            - name: Install Docker
              apt: 
                name: docker-ce
                state: latest

            - name: Put user
              command: "usermod -aG docker $USER"


Dejo un tutorial de como instalar Docker [sin sudo](https://www.digitalocean.com/community/tutorials/como-instalar-y-usar-docker-en-ubuntu-18-04-1-es)

Hacemos dos archivos Dockerfile, uno con Ruby:

        FROM ruby:2.6.0

        MAINTAINER Matilde Cabrera <mati331@correo.ugr.es>

        # lanzar errores si Gemfile ha sido modificado desde Gemfile.lock
        RUN bundle config --global frozen 1

        RUN mkdir /CC-WebProject
        WORKDIR /CC-WebProject
        ENV HOME /CC-WebProject

        COPY Gemfile Gemfile.lock ./

        RUN gem install bundler -v 2.0.2
        RUN bundle install

        COPY . .

        # Comando predeterminado, ejecutando la aplicación como un servicio
        CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "5000"]

El segundo con Alpine:

        FROM alpine:latest

        MAINTAINER Matilde Cabrera <mati331@correo.ugr.es>

        RUN apk update && apk upgrade && apk add bash ruby-bundler && apk add ruby-full

        # lanzar errores si Gemfile ha sido modificado desde Gemfile.lock
        RUN bundle config --global frozen 1

        # genera la carpeta CC-WebProject
        RUN mkdir /CC-WebProject    
        # directorio destino donde se copiará nuestro proyecto
        WORKDIR /CC-WebProject

        # copia los archivos referidos del directorio local a la imagen docker
        COPY Gemfile Gemfile.lock ./

        RUN bundle install 

        # copia los archivos de la fuente local (el directorio actual) al directorio definido por WORDIR 
        COPY . .

        # expone el puerto 5000
        EXPOSE 5000

        # Comando predeterminado, ejecutando la aplicación como un servicio
        CMD ["rake","foreman","env=1"]
        # prueba en local
        #CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "5000"]

A destacar del archivo:

- Como Alpine viene con lo mínimo, primero actualizamos los repositorios, luego añadimos [bundler](https://pkgs.alpinelinux.org/package/edge/main/x86/ruby-bundler) y [ruby-full](https://pkgs.alpinelinux.org/package/edge/main/x86/ruby-full). Después de probar e instalar muchos paquetes, hemos preferido instalar solo ruby-full que tiene todas las dependencias necesarias para la instalación.

- Al copiar "COPY COPY Gemfile Gemfile.lock ./" y ejecutar "RUN bundle install", se crea una capa inferior de imagen, separada. con la siguientes instrucción "COPY . .", se copian los archivos de la app en la imagen. Esto implica que si alguno de los archivos de la capa inferior cambia, se puede reconstruir la imagen usando la misma de la caché. Mucho más eficiente que construir todo desde cero.

Hemos comparado los y nos quedamos con Alpine que tiene un tamaño menor:

![imagen](img/contenedor_images.png)

Construimos y lanzamos nuestro proyecto con Docker:

![imagen](img/contenedor_docker.png)

Entramos al contenedor para corregir algunos errores y lo probamos en local:

![imagen](img/contenedor_rake_foreman.png)

Alojamos nuestro contenedor Docker en [Docker-hub](https://hub.docker.com/r/mati3/webproject), Docker-hub es una plataforma donde podemos alojar aplicaciones desde nuestro equipo. Tan solo tenemos que entrar, puesto que ya tenemos cuenta, incluir el repositorio asignándole un nombre y enlazándola a nuestro GitHub:

![imagen](img/contenedor_dockerHub.png)

Ajustamos para un autobuild, que se refresque automáticamente cada vez que hacemos un push en GitHub:

![imagen](img/contenedor_autobuild_hub.png)

De igual forma usamos [Heroku](https://dashboard.heroku.com/apps/cc-webproject) como PaaS, su uso es muy fácil ademas gratuito, los servicios tienen una conexión HTTPS lo que le da un protocolo seguro. Es una infraestructura estable garantizada por [AWS](https://aws.amazon.com/marketplace/pp/Heroku-Inc-Heroku-Cloud-Application-Platform/B008DJG1TY#product-description).

[Heroku](https://devcenter.heroku.com/) es compatible con multitud de lenguajes de programación con Ruby, Java, Python, Node.js, etc. Es multiplataforma y lo mas importante admite git privados. 

Por todo ello es una excelente opción para el desarrollo de una aplicación.

Creamos una nueva app:

![imagen](img/contenedor_heroku_1.png)

La enlazamos a nuestro repositorio de Github:

![imagen](img/contenedor_heroku_2.png)

Desplegamos la app:

![imagen](img/contenedor_heroku_3.png)

Podemos probar nuestra aplicación con las siguientes rutas:

        https://cc-webproject.herokuapp.com/                     
        https://cc-webproject.herokuapp.com/todos
        https://cc-webproject.herokuapp.com/producto/00101
        https://cc-webproject.herokuapp.com/producto/00102
        https://cc-webproject.herokuapp.com/producto/00103
        https://cc-webproject.herokuapp.com/producto/00104

Probamos su funcionamiento:

![imagen](img/contenedor_navegador.png)

![imagen](img/contenedor_navegador_2.png)