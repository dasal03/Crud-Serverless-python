import json
from db import *
from sqlalchemy import Column, Integer, Date, String, ForeignKey, Float

class Producto(Base):
  __tablename__ = 'producto'

  id = Column(Integer, primary_key=True)
  producto = Column(String)
  valor = Column(Float)

  def __init__(self, 
          producto, 
          valor) -> None:

    self.producto = producto
    self.valor = valor

  def __repr__(self) -> str:

    prod = {
      "id": self.id,
      "producto": self.producto,
      "valor": self.valor
    }

    return json.dumps(prod)