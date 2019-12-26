#!/usr/bin/env python
# coding: utf-8

import unittest
import json
import sys, os.path

dir_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))+ '/src/')
sys.path.append(dir_path)

from dbclientes import dbClientes
from pymongo import MongoClient

def db():
    c = MongoClient('localhost', None)
    con = c.baseDeDatos
    db = dbClientes(con.Clientes)
    return db

class TestdbClientes(unittest.TestCase): 

    def test_insertClient(self):
        self.assertEqual(db().insertClient("jj@ugr.es"), "Usuario registrado : jj@ugr.es", "usuario no registrado")
        self.assertEqual(db().insertClient("jj@ugr.es"), "Usuario existente, operación no valida", "usuario existente error")

    def test_insertCesta(self):
        self.assertEqual(db().insertCesta("jj@ugr.es","00105"), "articulo no encontrado", "articulo no encontrado error")

    def test_get(self):
        self.assertIsNot(db().getAll(), [], "base de datos vacía error")
        self.assertIsNot(db().getClientes(), [], "sin clientes error")
        self.assertIsNot(db().getCesta("jj@ugr.es"), [], "cesta vacía error")

    def test_delete(self):
        self.assertEqual(db().deleteClient("jj@ugr.es"), 0, "user no borrado error")
