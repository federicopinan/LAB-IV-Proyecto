from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from routers.categoria import categoria_router
from routers.libro import libro_router
from routers.prestamo import prestamo_router
from routers.usuario import usuario_router
from starlette.middleware.cors import CORSMiddleware
from middlewares.error_handler import ErrorHandler

app = FastAPI()
app.version = "1.0.0"
app.description = "TPI de la materia Laboratorio IV - Backend y Frontend"

#? Definmos los origenes que van a poder consultar el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #* Habilitamos los dominios para realizar consultas
    allow_credentials=True, #* Habilitamos cookies y encabezados de autentificacion
    allow_methods=["*"],#* Habilitamos métodos HTTP( GET, POST, PUT, HEAD, OPTION, etc)
    allow_headers=["*"],#* Habilitamos encabezados para enviar desde un navegador.
)
#! Routers de las entidades
app.include_router(categoria_router)
app.include_router(libro_router)
app.include_router(prestamo_router)
app.include_router(usuario_router)

app.add_middleware(ErrorHandler)

#! Creamos las tablas en la base de datos
Base.metadata.create_all(bind=engine)

#! Endpoint raíz de prueba
@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello world</h1>')


import uvicorn 

if __name__ == "__main__":
	uvicorn.run(app, host="127.0.0.1", port=8000)