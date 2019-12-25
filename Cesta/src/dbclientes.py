#from cestacliente import Cestacliente
from src.catalogo import Catalogo
import json
from pymongo import MongoClient

class dbClientes:
    def __init__(self, collection):
        self.client = collection
        self.ct = Catalogo()


    def insertClient(self, correo_id):
        clientes = self.client.find({},{"cesta":1,"_id":1})
        salida = "ok"
        for c in clientes:
            if correo_id == c['_id'] :
                salida = "Usuario existente, operación no valida"
        if salida == "ok" :
            cesta = []
            # x = Cestacliente(correo_id)
            # client.insert({x})
            self.client.insert_one({'_id':correo_id,'cesta':cesta})
            salida = "Usuario registrado : " + correo_id
        return  salida 

    def insertCesta(self, correo_id, cesta_id):
        if self.ct.isArticulo(cesta_id):
            newcesta = self.client.aggregate([{"$match":{"_id": correo_id}} ,{ "$addFields":{"cesta":{"$concatArrays":["$cesta",[self.ct.json(cesta_id)]]}}}])
            return list(newcesta)
        else:
            return "articulo no encontrado"        


    def getAll(self):
        clientes = self.client.find({},{"cesta":1,"_id":1})
        salida = []
        for c in clientes:
            salida.append(c)
        return  salida

    def getClientes(self):
        clientes = self.client.find({},{"cesta":1,"_id":1})
        salida = []
        for c in clientes:
            salida.append(c['_id'])
        return  salida

    def getCesta(self, correo_id):
        clientes = self.client.find({"_id": correo_id},{"cesta":1,"_id":0})
        salida = []
        for c in clientes:
            salida.append(c['cesta'])
        return salida

    def deleteClient(self, correo_id):
        self.client.delete_one({"_id": correo_id})
        return self.client.count_documents({"_id": correo_id})


