import json
from clase_pedidos import pedido_class

def pedidos(event, context):
    body = json.loads(event["body"])

    nombre = body["nombre"]
    fecha = body["fecha"]
    id_producto = body["id_producto"]
    cantidad = body["cantidad"]
    valor_total = body["valor_total"]
    direccion = body["direccion"]
    ciudad = body["ciudad"]
    telefono = body["telefono"]
    estado = body["estado"]

    ped = pedido_class()

    agregar = ped.crear_pedidos(nombre, fecha, id_producto, cantidad, valor_total, direccion, ciudad, telefono, estado)

    body = {
        "pedido": body
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response