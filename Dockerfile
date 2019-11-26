FROM alpine:latest

MAINTAINER Matilde Cabrera <mati331@correo.ugr.es>

RUN apk update && apk upgrade && apk add bash ruby-bundler && apk add ruby-full

# lanzar errores si Gemfile ha sido modificado desde Gemfile.lock
RUN bundle config --global frozen 1

RUN mkdir /CC-WebProject
WORKDIR /CC-WebProject

COPY Gemfile Gemfile.lock ./

RUN bundle install 

COPY . .

# expone el puerto 5000, prueba en local
EXPOSE 5000

# Comando predeterminado, ejecutando la aplicación como un servicio
#CMD ["rake","foreman","env=1"]
# prueba en local
CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "5000"]
