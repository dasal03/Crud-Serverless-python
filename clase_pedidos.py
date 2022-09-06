from modelos.Pedidos import Pedidos
from db import session

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
                estado):
      try:

        self.session = session

        self.pedido = Pedidos(nombre, fecha, id_producto, cantidad, valor_total, direccion, ciudad, telefono, estado)
        self.session.add(self.pedido)
        self.session.commit()
        self.session.close()
        return True

      except Exception as e:
        print(e)
        return e

  def obtener_pedidos(self, id_producto):
    pedido = session.query(Pedidos).all()

    return pedido