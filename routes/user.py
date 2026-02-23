from fastapi import APIRouter 
from models.user import User
from config.db import conn
from schemas.user import userEntity ,usersEntity

user = APIRouter()

@user.get('/')
async def find_all_users():
   return usersEntity(conn.proyectodb.users.find())

@user.post('/')
async def create_user(user : User):
    nuevo_usuario = dict(user)
    # Insertar en la nueva colección
    id_insertado = conn.proyectodb.users.insert_one(nuevo_usuario).inserted_id
    
    # Buscar el documento único creado usando el ID
    usuario_encontrado = conn.proyectodb.users.find_one({"_id": id_insertado})
    return userEntity(usuario_encontrado)




