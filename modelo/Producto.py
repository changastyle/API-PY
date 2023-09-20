from sqlalchemy.orm import relationship

from modelo.Foto import Foto

from sqlalchemy import Boolean, Column, Text, Integer, String, ForeignKey
from UTILS.ConexionDB import BaseEntity

class Producto(BaseEntity):
    __tablename__ = "productos"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    nombre = Column(Text)
    precio = Column(Text)
    foto = Column(Integer, ForeignKey(Foto.id))
    relFoto = relationship(Foto, uselist=False)
    activo = Column(Boolean)

    # nombre: str
    # precio: int
    # foto: Foto
    # activo: bool

    def __init__(self , nombre: str , precio: int , foto: Foto , activo: bool):
        self.nombre = nombre
        self.precio = precio
        self.foto = foto
        self.activo = activo
