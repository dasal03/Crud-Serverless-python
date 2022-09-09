from modelos.Estado import Estado
from modelos.Pedidos import Pedidos
from db import session
from modelos.Productos import Producto

class pedido_class():

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

        self.session = session

        self.pedido = Pedidos(nombre, fecha, id_producto, cantidad, valor_total, direccion, ciudad, telefono, id_estado)
        self.session.add(self.pedido)
        self.session.commit()
        self.session.close()
        return True

      except Exception as e:
        print(e)
        return e

  def obtener_pedidos(self, id_producto=0):
    pedido = session.query(Pedidos, Estado.estado.label("estado_nombre"),Producto.producto).join(Estado, Pedidos.id_estado == Estado.id)
    pedido = pedido.join(Producto, Pedidos.id_producto == Producto.id)
    
    pedido = pedido.all()

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
    pedido = session.query(Pedidos).all()

    return pedido