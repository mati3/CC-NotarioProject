#!/usr/bin/env python
# coding: utf-8

import unittest
import json
import sys, os.path

dir_path = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(dir_path)

from appCesta import *

class TestAppCesta(unittest.TestCase): 

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_Hello_World(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World !', response.data) # b pasa el string a bytes

    def test_newclient(self):
        response = self.app.post('/newclient/jj@ugr.es')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'jj@ugr.es', response.data)

    def test_newcesta(self):
        response = self.app.post('/newcesta/jj@ugr.es/00101')
        self.assertEqual(response.status_code, 200)

    def test_cesta(self):
        response = self.app.get('/cesta/jj@ugr.es')
        self.assertEqual(response.status_code, 200)

    def test_clientes(self):
        response = self.app.get('/clientes')
        self.assertEqual(response.status_code, 200)

    def test_All(self):
        response = self.app.get('/todo')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.app.get('/delete/jj@ugr.es')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'0', response.data)
