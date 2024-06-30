from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from database import engine, Base
from routers.categoria import categoria_router
from routers.libro import libro_router
from routers.prestamo import prestamo_router
from routers.usuario import usuario_router

app = FastAPI()

app.include_router(categoria_router)
app.include_router(libro_router)
app.include_router(prestamo_router)
app.include_router(usuario_router)

Base.metadata.create_all(bind=engine)