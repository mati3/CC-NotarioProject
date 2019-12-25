#!/usr/bin/env python
# coding: utf-8
from flask import jsonify
import requests
import json

class Catalogo:
    
    def __init__ (self):
        todo = requests.get('http://localhost:5000/todos')
        self.catalogo= []
        iden = []
        en = ["Articulo","Descripcion","Estado de la compra","Estado del pago", "Cantidad"]
        for c in todo.json():
            iden.append(c["identificador"])
            iden.append(c['descripcion'] + " precio " + c['precio'] + " peso " + c['peso'] + " volumen " + c['volumen'])
            iden.append("En proceso")
            iden.append("En proceso")
            iden.append("1")
            self.catalogo.append(dict(zip(en,iden)))
            iden = []
        self.catalogo= json.dumps(self.catalogo)

        
    def getCatalogo(self):
        return self.catalogo

    def isArticulo(self, art):
        for c in json.loads(self.getCatalogo()):
            if c["Articulo"]==art:
                return True
        return False
    
    def getDescripcion(self, art):
        for c in json.loads(self.getCatalogo()):
            if c["Articulo"]==art:
                return c["Descripcion"]
        return False
    
    def json(self, art):
        for c in json.loads(self.getCatalogo()):
            if c["Articulo"]==art:
                return c
        return False


new = Catalogo()
print(json.loads(new.getCatalogo()))
#for c in json.loads(new.getCatalogo()):
#  if new.isArticulo(c["Articulo"]):
#    print(new.getDescripcion(c["Articulo"]))
#print(new.isArticulo("00109"))
#print(new.getDescripcion("00109"))
#print(new.json("00101"))
