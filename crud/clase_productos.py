from modelos.Productos import Producto
from db import session


class producto_class():

    def crear_productos(self, producto, valor):
        try:

            self.session = session

            self.producto = Producto(producto, valor)
            self.session.add(self.producto)
            self.session.commit()
            self.session.close()
            return True

        except Exception as e:
            print(e)
            return e

    def obtener_productos(self, id):
        producto = session.query(Producto).all()

        return producto
