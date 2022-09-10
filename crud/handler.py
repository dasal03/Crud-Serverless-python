import json
from pedidos import pedidos
from productos import productos
from estado import estado


def handler(event, context):
    body = json.loads(event["body"])

    modulo = body["modulo"]
    if (modulo == "pedidos"):
        accion = pedidos(event=event, context=context)
    elif (modulo == "productos"):
        accion = productos(event=event, context=context)
    elif (modulo == "estado"):
        accion = estado(event=event, context=context)
    else:
        return "Módulo inválido"

    body = {
        "respuesta": accion
    }

    response = {"statusCode": 200, "headers": {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
                'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, Accept',
                'Content-Type': 'application/json'
            }, "body": json.dumps(body, default=str)}

    return response
