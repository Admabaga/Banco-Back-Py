from fastapi import FastAPI
from backbancopy.Controlador.UsuarioControlador import users_router
from app.services.user_service import UserService
from app.database import get_database

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    global db
    db = await get_database()

UserService(db)

app.include_router(users_router)
