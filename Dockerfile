FROM alpine:latest

LABEL maintainer="mati331@correo.ugr.es"

RUN mkdir /Catalogo
WORKDIR /Catalogo

RUN apk update && apk upgrade && apk add bash ruby-bundler && apk add ruby-full

# lanzar errores si Gemfile ha sido modificado desde Gemfile.lock
RUN bundle config --global frozen 1

COPY Catalogo/Gemfile Catalogo/Gemfile.lock ./

RUN bundle install 

COPY Catalogo .

# Comando predeterminado, ejecutando la aplicación como un servicio
CMD ["rake","foreman","env=1"]
# prueba en local
#CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "5000"]
