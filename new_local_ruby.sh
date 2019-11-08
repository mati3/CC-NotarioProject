#!/bin/bash
# -*- coding: utf-8 -*-

echo '###### Instalando curl ######'
sudo apt install curl -y

echo '###### Obteniendo keyserver para rvm ######'
gpg --keyserver hkp://pool.sks-keyservers.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3 7D2BAF1CF37B13E2069D6956105BD0E739499BDB

echo '###### Instalando rvm ######'
curl -sSL https://get.rvm.io | bash -s stable 

[ -s "$HOME/.rvm/scripts/rvm" ] && . "$HOME/.rvm/scripts/rvm" >> ~/.bash_profile
[ -r $rvm_path/scripts/completion ] && . $rvm_path/scripts/completion >> .bash_profile

echo '###### Instalando ruby-2.3.0 ######'
rvm install ruby-2.3.0

echo '###### Usando ruby-2.3.0 ######'
rvm use 2.3.0 # version minima para instalar bundler

echo '###### Obteniendo bundler ######'
gem install bundler

echo '###### Instalando bundle ######'
bundle install

echo '###### Instalación completada con el marco de trabajo para ruby ######'
echo '###### Para probar los test del proyecto ejecute: rake ######'
