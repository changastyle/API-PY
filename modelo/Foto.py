from sqlalchemy import Boolean, Column, Text, Integer, String, ForeignKey
from UTILS.ConexionDB import BaseEntity
class Foto(BaseEntity):
    __tablename__ = "fotos"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    urlProv=  Column(Text)
    # urlFull: str
    activo= Column(Boolean)

    def __init__(self , urlProv: str , activo: bool):
        self.urlProv = urlProv
        self.activo = activo
        self.urlFull = self.getFullFoto()
    def getFullFoto(self):
        urlFull = "http://localhost/upload/api-py/" + str(self.urlProv)
        return urlFull