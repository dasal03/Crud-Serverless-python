from clase_pedidos import pedido_class
from datetime import datetime


def pedidos(body):

    nombre = body["nombre"]
    fecha = datetime.now()
    id_producto = body["id_producto"]
    cantidad = body["cantidad"]
    valor_total = body["valor_total"]
    direccion = body["direccion"]
    ciudad = body["ciudad"]
    telefono = body["telefono"]
    id_estado = body["id_estado"]

    ped = pedido_class()
    
    pedido = ped.crear_pedidos(nombre, fecha, id_producto, cantidad,
                                valor_total, direccion, ciudad, telefono, id_estado)
  
    print(pedido)
    
   

    return pedido
