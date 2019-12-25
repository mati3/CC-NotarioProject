#!/usr/bin/env python
# coding: utf-8

import unittest
import json
import sys, os.path

dir_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))+ '/src/')
sys.path.append(dir_path)

from cestacliente import Cestacliente
from cesta import Cesta

class TestCestaCliente(unittest.TestCase): 

    def test_cestaCliente(self):

        c = Cesta("00101", "En proceso", "Completado", "Producto mini", "2")
        x = Cestacliente("matiii@ugr.es", c)
        y = Cestacliente("jj@ugr.es")

        self.assertEqual(x.getCorreo(), "matiii@ugr.es", "correo incorrecto")
        x.setCorreo("mat@ugr.es")
        self.assertEqual(x.getCorreo(),"mat@ugr.es", "correo incorrecto")

        self.assertEqual(y.getCesta(), [], "cesta incorrecta")
        
        self.assertTrue(y.setCesta(c))
        self.assertTrue(y.deleteCesta(c))
        self.assertTrue(y.setnewCesta("00102", "En proceso", "Completado", "Producto pequeño", "2"))
