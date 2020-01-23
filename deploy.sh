#!/bin/bash

var_catalogo="no"
var_cesta="no"

echo " "
read -p "Do you want to install the microservice Catalogo? [yN] " -n 1 -r
if [[ $REPLY =~ ^[Yy]$ ]]; then
var_catalogo="yes"
fi
echo " "
read -p 'Do you want to install microservice Cesta?[yN] ' -n 1 -r 
if [[ $REPLY =~ ^[Yy]$ ]]; then
var_cesta="yes"
fi
echo " "

if [[ $1 == 'up' ]]; then 
	var_cesta=$var_cesta var_catalogo=$var_catalogo vagrant up
elif [[ $1 == 'provision' ]]; then 
	var_cesta=$var_cesta var_catalogo=$var_catalogo vagrant provision
elif [[ $1 == 'azure' ]]; then 
	var_cesta=$var_cesta var_catalogo=$var_catalogo vagrant up --provider=azure

echo " " 
read -p 'Do you want to deploy all?[yN] ' -n 1 -r 

if [[ $REPLY =~ ^[Yy]$ ]]; then
fab -f despliegue/fabfile.py -H vagrant@ccwebproject.westeurope.cloudapp.azure.com Run
fi

elif [[ $1 == 'local' ]]; then 
	ansible-playbook --extra-vars "var_catalogo=$var_catalogo var_cesta=$var_cesta" --connection=local --inventory 172.0.0.1, workstation.yml
else
	echo " "
	echo -e "    \033[31mThe options of use are 'up', 'provision' or 'local'\033[0m"
	echo " "
	echo -e " 	Use '\033[33m./deploy up\033[0m' if it is the first and you want to use a virtual machine "
	echo " "
	echo -e " 	Use '\033[33m./deploy provision\033[0m' if you just have a virtual machine and you want to repeat the provision "
	echo " "
	echo -e " 	Use '\033[33m./deploy azure\033[0m' if you just have a virtual machine in Azure "
	echo " "
	echo -e " 	Use '\033[33m./deploy local\033[0m' if you want to be the install in your machine local "
fi

