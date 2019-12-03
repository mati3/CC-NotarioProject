FROM ruby:2.6.0

LABEL maintainer="mati331@correo.ugr.es"

RUN mkdir /Catalogo
WORKDIR /Catalogo
ENV HOME /Catalogo

# lanzar errores si Gemfile ha sido modificado desde Gemfile.lock
RUN bundle config --global frozen 1

COPY Catalogo/Gemfile Catalogo/Gemfile.lock ./

RUN gem install bundler -v 2.0.2
RUN bundle install

COPY Catalogo .

# Comando predeterminado, ejecutando la aplicación como un servicio
CMD ["rake","foreman","env=1"]
# prueba en local
#CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "5000"]
