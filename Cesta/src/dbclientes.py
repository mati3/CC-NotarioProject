#from cestacliente import Cestacliente
from src.catalogo import Catalogo
import json
from pymongo import MongoClient

class dbClientes:
    def __init__(self, collection):
        c = [{'Articulo': '00101', 'Descripcion': 'Producto mini precio 3 peso 0.5 kg volumen 5,5,30', 'Estado de la compra': 'En proceso', 'Estado del pago': 'En proceso', 'Cantidad': '1'}, {'Articulo': '00102', 'Descripcion': 'Producto pequeño precio 5 peso 1 kg volumen 10,10,40', 'Estado de la compra': 'En proceso', 'Estado del pago': 'En proceso', 'Cantidad': '1'}, {'Articulo': '00103', 'Descripcion': 'Producto mediano precio 10 peso 2 kg volumen 20,20,50', 'Estado de la compra': 'En proceso', 'Estado del pago': 'En proceso', 'Cantidad': '1'}, {'Articulo': '00104', 'Descripcion': 'Producto grande precio 20 peso 3 kg volumen 30,30,50', 'Estado de la compra': 'En proceso', 'Estado del pago': 'En proceso', 'Cantidad': '1'}]

        self.client = collection
        self.ct = Catalogo(c)


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


