import hashlib
import sqlite3 
import os 
from typing import List 
from fastapi import Depends, FastAPI, HTTPException, status 
from fastapi.security import HTTPBasic, HTTPBasicCredentials 
from pydantic import BaseModel 
from typing import Union  
from fastapi.middleware.cors import CORSMiddleware   #Libreria


app = FastAPI() 

DATABASE_URL = os.path.join("sql/clientes.sqlite") 

security = HTTPBasic() 

class Usuarios(BaseModel): 
    username: str 
    level: int 

class Respuesta (BaseModel) :  
    message: str  
           
class Cliente (BaseModel):  
    id_cliente: int  
    nombre: str  
    email: str  

origins = [
    "https://8000-katiaolem-apirest2-qwcr8ep7p9d.ws-us51.gitpod.io/",
    "https://8081-katiaolem-apirest2-qwcr8ep7p9d.ws-us51.gitpod.io/"
    "http://localhost:8080",   #lista de donde se recibiran
    "http://127.0.0.1:3000", 
    "*"
      
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/", response_model=Respuesta) 
async def index(): 
    return {"message": "API REST"} 


def get_current_level(credentials: HTTPBasicCredentials = Depends(security)):
    password_b = hashlib.md5(credentials.password.encode())
    password = password_b.hexdigest()
    with sqlite3.connect(DATABASE_URL) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT level FROM usuarios WHERE username = ? and password = ?",
            (credentials.username, password),)
        user = cursor.fetchone()
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
    return user[0] #ADMIN

@app.get("/clientes/", response_model=List[Cliente],status_code=status.HTTP_202_ACCEPTED,
summary="Lista de usuarios",description="Retorna una lista de usuarios")
async def clientes(level: int = Depends(get_current_level)):
    if level == 1: 
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM clientes')
            response = cursor.fetchall()
            return response
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have permission to access this resource",
            headers={"WWW-Authenticate": "Basic"},
        )

@app.get("/clientes/{id}", response_model=List[Cliente],status_code=status.HTTP_202_ACCEPTED,
summary="Retorna lista de usuarios",description="Retorna una lista de usuarios")
async def clientes(level: int = Depends(get_current_level),id_cliente: int=0):
    if level == 1: 
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM clientes WHERE id_cliente={}".format(id_cliente))
            response = cursor.fetchall()
            return response
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have permission to access this resource",
            headers={"WWW-Authenticate": "Basic"},
        )


@app.post("/clientes/", response_model=Respuesta,status_code=status.HTTP_202_ACCEPTED,
summary="Agrega un usuario",description="Agrega un usuario")
async def clientes(level: int = Depends(get_current_level),nombre: str="", email:str=""):
    if level == 0: 
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("INSERT INTO clientes (nombre, email) VALUES (? , ?);",(nombre, email))
            connection.commit()
            response = {"message":"Cliente agregado"}
            return response
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have permission to access this resource",
            headers={"WWW-Authenticate": "Basic"},
        )

@app.put("/clientes/", response_model=Respuesta,status_code=status.HTTP_202_ACCEPTED,
summary="Actualiza un usuario",description="Actualiza un usuario")
async def clientes(level: int = Depends(get_current_level), id_cliente: int=0, nombre: str="", email:str=""):
    if level == 0: 
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("UPDATE clientes SET nombre =?, email= ? WHERE id_cliente =?;",(nombre, email, id_cliente))
            connection.commit()
            response = {"message":"Cliente actualizado"}
            return response
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have permission to access this resource",
            headers={"WWW-Authenticate": "Basic"},
        )


@app.delete("/clientes/", response_model=Respuesta,status_code=status.HTTP_202_ACCEPTED,
summary="Elimina un usuario",description="Elimina un usuario")
async def clientes(level: int = Depends(get_current_level), id_cliente: int=0):
    if level == 0: 
        with sqlite3.connect(DATABASE_URL) as connection:
            connection.row_factory = sqlite3.Row
            cursor = connection.cursor()
            cursor.execute("DELETE FROM clientes WHERE id_cliente= '{id_cliente}';".format(id_cliente=id_cliente))
            connection.commit()
            response = {"message":"Cliente borrado"}
            return response
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Don't have permission to access this resource",
            headers={"WWW-Authenticate": "Basic"},
        )