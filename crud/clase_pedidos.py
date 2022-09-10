from modelos.Estado import Estado
from modelos.Pedidos import Pedidos
from db import session
from modelos.Productos import Producto


class pedido_class():

  def __init__(self) -> None:
      self.session = session

  def crear_pedidos(self,
                    nombre,
                    fecha,
                    id_producto,
                    cantidad,
                    valor_total,
                    direccion,
                    ciudad,
                    telefono,
                    id_estado):

    try:
        print(nombre)

        session = self.session

        pedido = Pedidos(nombre, fecha, id_producto, cantidad,
                              valor_total, direccion, ciudad, telefono, id_estado)
        print(pedido)
        session.add(pedido)
        session.commit()
        session.close()
        print("paso de crear")
        return True

    except Exception as e:
        print(e)
        return e

  def obtener_pedidos(self, id_producto=0):

    session = self.session
    pedido = session.query(Pedidos, Estado.estado.label(
        "estado_nombre"), Producto.producto).join(Estado, Pedidos.id_estado == Estado.id)
    pedido = pedido.join(Producto, Pedidos.id_producto == Producto.id)

    pedido = pedido.all()
    session.close()

    pedidos = []

    for p in pedido:
        pedidos.append({
            'nombre': p.Pedidos.nombre,
            'fecha': p.Pedidos.fecha.strftime('%Y-%m-%d %H:%M:%S'),
            'cantidad': p.Pedidos.cantidad,
            'valor_total': p.Pedidos.valor_total,
            'direccion': p.Pedidos.direccion,
            'ciudad': p.Pedidos.ciudad,
            'telefono': p.Pedidos.telefono,
            'estado_nombre': p.estado_nombre,
            'producto_nombre': p.producto
        })

    return pedidos

  def actualizar_pedidos(self, id_producto):
      pedido = self.session.query(Pedidos).all()

      return pedido
