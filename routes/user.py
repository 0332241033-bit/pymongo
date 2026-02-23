from fastapi import APIRouter 
from models.user import User
from config.db import conn
from schemas.user import serializeDict ,serializeList
from bson import ObjectId

user = APIRouter()

@user.get('/')
async def find_all_users():
   return serializeList(conn.proyectodb.users.find())

@user.get('/{id}')
async def find_one_user(id) :
   return serializeDict(conn.proyectodb.users.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_user(user : User):
    nuevo_usuario = dict(user)
    # Insertar en la nueva colección
    id_insertado = conn.proyectodb.users.insert_one(nuevo_usuario).inserted_id
    
    # Buscar el documento único creado usando el ID
    usuario_encontrado = conn.proyectodb.users.find_one({"_id": id_insertado})
    return serializeDict(usuario_encontrado)


@user.put('/{id}')
async def update_user(id,user:User):
   conn.proyectodb.users.find_one_and_update({"_id": ObjectId(id)} ,{"$set":dict(user)})
   return serializeDict(conn.proyectodb.users.find_one({"_id":ObjectId(id)})) 
  
@user.delete('/{id}')
async def delete_user(id,user:User):
   
   return serializeDict(conn.proyectodb.users.find_one_and_delete({"_id":ObjectId(id)})) 
