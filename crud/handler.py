import json
from pedidos import pedidos
from productos import productos
from estado import estado


def handler(event, context):
    body = json.loads(event["body"])

    modulo = body["modulo"]
    if (modulo == "pedidos"):
        accion = pedidos(body)
    elif (modulo == "productos"):
        accion = productos(body)
    elif (modulo == "estado"):
        accion = estado(body)
    else:
        accion = {
            "error": "Módulo inválido"
        }

    body = {
        "respuesta": accion
    }

    response = {"statusCode": 200, "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept',
                'Content-Type': 'application/json'
                }, "body": json.dumps(body)}

    return response
