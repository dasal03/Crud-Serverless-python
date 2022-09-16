import json
from clase_estado import estado_class


def estado(body):

    estado = body["estado"]

    stat = estado_class()

    stat.crear_estado(estado)
    

    return stat
