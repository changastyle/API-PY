from UTILS import DAO
from modelo import Foto

class FotoRepo:

    def __init__(self):
        print("FOTO REPO")

    @staticmethod
    def llamar(self):
        arrFotos = DAO.select(Foto)
        return arrFotos

    @staticmethod
    def save(self, fotoNva):
        fotoNva = DAO.save(fotoNva)
        return fotoNva
