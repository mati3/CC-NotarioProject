#!/usr/bin/env python
# coding: utf-8

import json
from cesta import Cesta

class Cestacliente:
    
    def __init__ (self, corr, ces=None):
        self.id = corr
        self.cesta = []
        if ces is not None:
            self.cesta.append(ces.json())
        
    def getCorreo(self):
        return self.id

    def setCorreo(self, cor):
        self.id = cor
    
    def getCesta(self):
        return self.cesta

    def setCesta(self, ces):
        self.cesta.append(ces.json())
        if ces.json() in self.cesta:
            return True
        return False

    def setnewCesta(self, art, com, pag, descrip, cant): 
        x = Cesta(art, com, pag, descrip, cant)
        self.cesta.append(x.json())
        if x.json() in self.cesta:
            return True
        return False

    def deleteCesta(self, c):
        if c.json() in self.cesta:
            self.cesta.remove(c.json())
            return True
        return False

    def json(self):
        datos =  {
	"_id": self.getCorreo(),
	"cesta": self.getCesta()
    }
        return datos

#x = Cestacliente("matiii@ugr.es")
#print("sin cesta")
#print(x.json())
#y = Cesta("00101","en proceso","en proceso","producto","1")
#x.setCesta(y)
#x.setnewCesta("00102","en proceso","en proceso","producto","1")
#print("dos cestas")
#print(x.json())
#j = Cesta("00102","en proceso","en proceso","producto","1")
#print(j.json())
#x.deleteCesta(j.json())
#print("borro una cesta")
#print(x.json())
