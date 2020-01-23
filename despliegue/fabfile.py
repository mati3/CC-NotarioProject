# coding: utf-8

from fabric.api import *

def Remove():
	run('sudo rm -rf ./CC-WebProject')

def Install():
	Remove()
	run('git clone https://github.com/mati3/CC-WebProject.git')
	run('cd CC-WebProject/Catalogo && bundle install')
	run('pip3 install -r CC-WebProject/Cesta/requirements.txt')
	
def Run():
	run('cd CC-WebProject/Catalogo && sudo bundle exec rackup ',pty=False)
	run('cd CC-WebProject/Cesta && gunicorn -w 1 appCesta:app')

def Update():
	Install()
	Run()


