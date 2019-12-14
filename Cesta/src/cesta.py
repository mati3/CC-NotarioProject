#!/usr/bin/env python
# coding: utf-8

class Cesta:
    
    def __init__ (self, art, com, pag, descrip, cant):
        self.articulo = art
        self.compra = com
        self.pago = pag
        self.descripcion = descrip
        self.cantidad = cant
        
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

    def getDescripcion(self):
        return self.descripcion

    def setDescripcion(self, desc):
        self.descripcion = desc

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cant):
        self.cantidad = cant
