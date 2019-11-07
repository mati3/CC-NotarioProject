#!/usr/bin/env python
# coding: utf-8

class Post:
    
    def __init__ (self, cor, art, com, pag):
        self.correo = cor
        self.articulo = art
        self.compra = com
        self.pago = pag
        
    def getCorreo(self):
        return self.correo

    def setCorreo(self, cor):
        self.correo = cor

    def getArticulo(self):
        return self.articulo

    def setArticulo(self, art):
        self.articulo = art
    
    def getCompra(self):
        return self.compra

    def setCompra(self, com):
        self.compra = com
    
    def getPago(self):
        return self.pago
    
    def setPago(self, pag):
        self.pago = pag
