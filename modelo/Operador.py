from typing import Optional

from UTILS.ConexionDB import BaseEntity
from sqlalchemy import Column, Text, Integer
from pydantic import BaseModel

class Operador(BaseEntity):
    __tablename__ = "operadores"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    nombre = Column(Text)
    clave = Column(Text)
    email = Column(Text, unique=True, index=True)


    def __init__(self , nombre , clave , email):
        self.nombre = nombre
        self.clave = clave
        self.email = email





# DTOS:
class OperadorSAVEDTO(BaseModel):
    nombre: str
    email: str
    clave: str

class OperadorDTO(BaseModel):


    # def __init__(self , obj):
    #     if str(type(obj)) == "None":
    #         id = -1
    #         nombre= "None"
    #         email= "None"
    #         clave = "None"

    id: Optional[int] = -1
    nombre: Optional[str] = "None"
    email: Optional[str] = "None"
    clave: Optional[str] = "None"
