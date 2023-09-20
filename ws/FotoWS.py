from fastapi import APIRouter
from modelo.Foto import Foto
import FotoREPO

RouterFoto = APIRouter( prefix="/foto",tags=["Foto"])

@RouterFoto.get("/", status_code=200, summary="Listar Fotos")
def listarFotos():

    repo = FotoREPO()
    arrFotos = repo.llamar()
    return arrFotos
    # arrFotos = llamar()
    # return arrFotos


@RouterFoto.post("/", status_code=200, summary="Create Foto")
def create_foto():

    fotoNva = Foto(urlProv="default.png",activo=True)
    repo = FotoREPO()
    fotoGuardada = repo.save(fotoNva)
    return fotoGuardada



    # operadorNVO = Operador(**userDTO.__dict__)
    #
    # operadorNVO = save(operadorNVO)
    #
    # return operadorNVO

# @Router.get("/select", status_code=200 ,summary="Listar Operadores")
# def listOperadores():
#
#     arrOperadores = select(Operador)
#
#     print("ARR OPERADORES:", str(arrOperadores))
#
#     return limpiarDictAlchemy(arrOperadores)
#
# # response_model=OperadorDTO
# # response_model=OperadorDTO
# @Router.get("/getByEmailAndClave/{email}/{clave}", status_code=200, summary="Buscar Operador por email y clave")
# def getByEmailAndPass(email: str, clave: str ):
#     # rta = {}
#
#     print("EMAIL:", str(email))
#     print("CLAVE:", str(clave))
#
#     operadorDB = (createSesion().query(Operador).where
#     (
#         ( Operador.email == email) &
#         ( Operador.clave == clave)
#     ).first())
#
#     # if operadorDB != None:
#     #     rta = operadorDB
#
#
#     print("operadorDB:", str(operadorDB))
#     # print("rta:", str(rta))
#
#     return limpiarDictAlchemy(operadorDB)

# def create_user(userDTO: OperadorSAVEDTO , session:Session = Depends(gen_session)):
#
#     operadorNVO = Operador(**userDTO.__dict__)
#
#     session.add(operadorNVO)
#     session.commit()
#     session.refresh(operadorNVO)
#
#     return operadorNVO




    # arrProductos = [
    #     {"id":1,"nombre":"Ensalada de Frutas","precio":250},
    #     {"id":2,"nombre":"Ensalada de Frutillas","precio":350},
    #     {"id":3,"nombre":"Pollo","precio":150}
    #     ]
    #
    # return arrProductos