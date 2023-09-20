import uvicorn
from fastapi import FastAPI

from starlette.responses import RedirectResponse

from modelo import Foto , Producto
from modelo.Producto import Producto
from ws.Foto2WS import RouterFoto2
from ws.FotoWS import RouterFoto
from ws.OperadorWS import Router

from UTILS.ConexionDB import BaseEntity, engine

BaseEntity.metadata.create_all(engine)

app = FastAPI(
    title="API de Nico en Python",
    docs_url="/swagger"
)

# SQLALCHEMY_DATABASE_URL = f"mysql://root:{mysqlPass}@mysql/clinicapp-py"
SCHEMA = "clinicapp-py"

@app.get("/")
def index():
    response = RedirectResponse(url='/swagger')
    return response
@app.get("")
def index2():
    response = RedirectResponse(url='/swagger')
    return response
@app.get("/lista")
def serialize_lista():
    lista = ["Producto 1", "Producto 2", "Producto3"]
    return lista
@app.get("/diccionario")
def serialize_diccionario():
    # , "nombre": "Producto2", "nombre": "Producto 3"
    diccionario = {"nombre":"Producto 1"}
    return diccionario
@app.get("/objeto")
def serialize_objeto():
    # , "nombre": "Producto2", "nombre": "Producto 3"
    fotoDefault = Foto(urlProv="default.png",activo=True)
    producto1 = Producto(nombre="Frutillas",precio=250,foto=fotoDefault, activo=True)
    return producto1

app.include_router(Router)
app.include_router(RouterFoto)
app.include_router(RouterFoto2)




if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)