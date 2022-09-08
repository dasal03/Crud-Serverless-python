import json
from clase_productos import producto_class

def productos(event, context):
  body = json.loads(event["body"])

  producto = body["producto"]
  valor = body["valor"]

  prodos = producto_class()

  agregar = prodos.crear_productos(producto, valor)

  body = {
      "producto": body
  }

  response = {"statusCode": 200, "body": json.dumps(body)}
  
  return response