import json
from db import *
from sqlalchemy import Column, Integer, String


class Estado(Base):
    __tablename__ = 'estado'

    id = Column(Integer, primary_key=True)
    estado = Column(String)

    def __init__(self, estado):
        self.estado = estado

    def __repr__(self) -> str:

        status = {
            'estado': self.estado
        }

        return json.dumps(status)
