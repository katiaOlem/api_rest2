from fastapi import FastAPI 
from typing import Union 
import sqlite3 
from typing import List 
from pydantic import BaseModel 
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


app = FastAPI()   #objeto


  
class Respuesta (BaseModel) : 
     message: str 
          
  
class Cliente (BaseModel): 
     id_cliente: int 
     nombre: str 
     email: str 
  
class ClienteID(BaseModel):
    nombre: str
    email : str


app =FastAPI() 
  
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
  
@app.get("/clientes/") 
async def clientess(): 
     with sqlite3.connect('sql/clientes.sqlite') as connection: 
         connection.row_factory = sqlite3.Row 
         cursor=connection.cursor() 
         cursor.execute("SELECT * FROM clientes") 
         response=cursor.fetchall() 
         return response 
         return {"message": "API REST"} 
  
@app.get("/clientes/{id}") 
async def clientes(id): 
     with sqlite3.connect('sql/clientes.sqlite') as connection: 
         connection.row_factory = sqlite3.Row 
         cursor=connection.cursor() 
         cursor.execute("SELECT * FROM clientes WHERE id_cliente={}".format(int(id))) 
         response=cursor.fetchall() 
         return response

@app.post("/clientes/", response_model=Respuesta)
def post_cliente(cliente: ClienteID):
    with sqlite3.connect('sql/clientes.sqlite') as connection:
        connection.row_factory = sqlite3.Row
        cursor=connection.cursor()
        cursor.execute("INSERT INTO clientes(nombre,email) VALUES(?,?)", (cliente.nombre,cliente.email))
        cursor.fetchall()
        response = {"message":"Cliente agregado"}
        return response


@app.put("/clientes/", response_model=Respuesta) #agregar
async def clientes_update(nombre: str="", email:str="", id_cliente:int=0):
    with sqlite3.connect("sql/clientes.sqlite") as connection:
        connection.row_factory = sqlite3.Row
        cursor = connection.cursor()
        cursor.execute("UPDATE clientes SET nombre =?, email= ? WHERE id_cliente =?;",(nombre, email, id_cliente))
        cursor.fetchall()
        response = {"message":"Cliente actualizado"}
        return response


@app.delete("/clientes/{id}")  #eliminar
async def clientes(id): 
     with sqlite3.connect('sql/clientes.sqlite') as connection: 
         connection.row_factory = sqlite3.Row 
         cursor=connection.cursor() 
         cursor.execute("DELETE FROM clientes WHERE id_cliente={}".format(int(id))) 
         cursor.fetchall() 
         response = {"message":"Cliente borrado"}
         return response