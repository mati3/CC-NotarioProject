#!/usr/bin/env python
# coding: utf-8

import unittest
import json
import sys, os.path

dir_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))+ '/src/')
sys.path.append(dir_path)

import unittest

from cesta import Cesta

class TestCesta(unittest.TestCase): 

    def test_cesta(self):
        #with open('ejemploCesta.json','r') as myfile:
         #   obj = myfile.read()
          #  c = Cesta(obj['Correo'], obj['Articulo'], obj['Estado de la compra'], obj['Estado del pago'])
        c = Cesta("00101", "En proceso", "Completado", "Producto mini", "2")

        self.assertEqual(c.getArticulo(), "00101", "articulo incorrecto")
        self.assertEqual(c.getCompra(),"En proceso", " estado de la compra incorrecta ")
        self.assertEqual(c.getPago(),"Completado", "estado del pago incorrecto")
        self.assertEqual(c.getDescripcion(),"Producto mini", "descripcion incorrecta")
        self.assertEqual(c.getCantidad(),"2", "cantidad incorrecta")
