#!/bin/bash
# -*- coding: utf-8 -*-

echo '###### Instalando pip3 ######'
sudo apt install python3-pip -y

echo '###### Instalando virtualenv ######'
sudo pip3 install virtualenv

echo '###### Creando carpeta lenv para marco de trabajo ######'
virtualenv lenv -p python3

echo '###### Activando carpeta lenv para marco de trabajo ######'
source lenv/bin/activate

echo '###### Instalando los requerimientos ######'
pip3 install -r requirements.txt

echo '###### Instalación completada con el marco de trabajo para python ######'
echo ' Para activar el parco de trabajo ejecute en su terminal: '
echo '		source lenv/bin/activate '
echo ' Para ejecutar la batería de test ejecute en su terminal: '
echo '		pytest '

