from modelos.Estado import Estado
from db import session


class estado_class():

    def crear_estado(self, estado):

        try:

            self.session = session

            self.estado = Estado(estado)
            self.session.add(self.estado)
            self.session.commit()
            self.session.close()
            return True

        except Exception as e:
            print(e)
            return e

    def get_estado(self):
        session.query(Estado).all()

    def actualizar_estado(self):
        session.query(Estado).all()
