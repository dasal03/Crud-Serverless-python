from clase_estado import estado_class


def estado(body):

    estado = body["estado"]

    stat = estado_class()

    agregar = stat.crear_estado(estado)
    print(agregar)


    return agregar
