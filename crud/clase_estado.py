from modelos.Estado import Estado
from db import session


class estado_class():

  def crear_estado(self, estado):

      try:

          self.session = session

          self.estado = Estado(estado)
          self.session.add(self.estado)
          self.session.commit()
          id_estado = self.estado.id
          self.session.close()
          if id_estado != "" and id_estado != None:
            return f"Operacion exitosa"
          else:
            return f"No se pudo insertar"

      except Exception as e:
          print(e)
          return e

  def obtener_estados(self, id):
     estado = session.query(Estado).all()

     return estado
        