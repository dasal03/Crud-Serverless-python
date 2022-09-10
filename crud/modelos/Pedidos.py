import json
from db import *
from sqlalchemy import Column, Integer, DateTime, String, Float


class Pedidos(Base):
    __tablename__ = 'pedidos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    fecha = Column(DateTime)
    id_producto = Column(Integer)
    cantidad = Column(String)
    valor_total = Column(Float)
    direccion = Column(String)
    ciudad = Column(String)
    telefono = Column(String)
    id_estado = Column(String)

    def __init__(self,
                 nombre,
                 fecha,
                 id_producto,
                 cantidad,
                 valor_total,
                 direccion,
                 ciudad,
                 telefono,
                 id_estado) -> None:

        self.nombre = nombre
        self.fecha = fecha
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.valor_total = valor_total
        self.direccion = direccion
        self.ciudad = ciudad
        self.telefono = telefono
        self.id_estado = id_estado

    def __repr__(self) -> str:

        cliente = {
            'nombre': self.nombre,
            'fecha': self.fecha.strftime('%Y-%m-%d %H:%M:%S'),
            'id_producto': self.id_producto,
            'cantidad': self.cantidad,
            'valor_total': self.valor_total,
            'direccion': self.direccion,
            'ciudad': self.ciudad,
            'telefono': self.telefono,
            'id_estado': self.id_estado
        }

        return json.dumps(cliente)
