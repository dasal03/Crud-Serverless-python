import json
from clase_estado import estado_class

def estado(event, context):
  body = json.loads(event["body"])

  estado = body["estado"]

  stat = estado_class()

  agregar = stat.crear_estado(estado)

  body = {
    "estado": estado
  }

  response = {"statusCode": 200, "body": json.dumps(body)}

  return response