import json
from clase_productos import producto_class


def productos(body):

    producto = body["producto"]
    valor = body["valor"]

    prodos = producto_class()
    
    agregar = prodos.crear_productos(producto, valor)
    print(agregar)


    return agregar
