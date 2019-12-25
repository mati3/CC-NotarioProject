#!/usr/bin/env python
# coding: utf-8

import unittest
import json
import sys, os.path

dir_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))+ '/src/')
sys.path.append(dir_path)

from catalogo import Catalogo

class TestCatalogo(unittest.TestCase): 

    def test_catalogo(self):
        c = [{'Articulo': '00101', 'Descripcion': 'Producto mini precio 3 peso 0.5 kg volumen 5,5,30', 'Estado de la compra': 'En proceso', 'Estado del pago': 'En proceso', 'Cantidad': '1'}, {'Articulo': '00102', 'Descripcion': 'Producto pequeño precio 5 peso 1 kg volumen 10,10,40', 'Estado de la compra': 'En proceso', 'Estado del pago': 'En proceso', 'Cantidad': '1'}, {'Articulo': '00103', 'Descripcion': 'Producto mediano precio 10 peso 2 kg volumen 20,20,50', 'Estado de la compra': 'En proceso', 'Estado del pago': 'En proceso', 'Cantidad': '1'}, {'Articulo': '00104', 'Descripcion': 'Producto grande precio 20 peso 3 kg volumen 30,30,50', 'Estado de la compra': 'En proceso', 'Estado del pago': 'En proceso', 'Cantidad': '1'}]
        cat = Catalogo(c)

        self.assertTrue(cat.isArticulo("00101"))
        self.assertTrue(cat.isArticulo("00102"))
        self.assertTrue(cat.isArticulo("00103"))
        self.assertTrue(cat.isArticulo("00104"))
        self.assertEqual(cat.getDescripcion("00101"),"Producto mini precio 3 peso 0.5 kg volumen 5,5,30", "descripcion incorrecta")
        self.assertEqual(cat.getDescripcion("00102"),"Producto pequeño precio 5 peso 1 kg volumen 10,10,40", "descripcion incorrecta")
        self.assertEqual(cat.getDescripcion("00103"),"Producto mediano precio 10 peso 2 kg volumen 20,20,50", "descripcion incorrecta")
        self.assertEqual(cat.getDescripcion("00104"),"Producto grande precio 20 peso 3 kg volumen 30,30,50", "descripcion incorrecta")
