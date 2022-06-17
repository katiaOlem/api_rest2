
from fastapi.testclient import TestClient
from code.main import app
import requests

clientes = TestClient(app)



def test_index():
    response = clientes.get("/") #request#
    data = {"message":"API REST"}
    assert response.status_code == 200 ##petición enviada ok
    assert response.json() == data

def test_clientes():
    response = clientes.get("/clientes/")  
    data =[{"id_cliente":1,"nombre":"Katia","email":"kat160417@gmail.com"},
    {"id_cliente":2,"nombre":"Itzel","email":"itezel16@gmail.com"},
    {"id_cliente":3,"nombre":"Leo","email":"leo17@gmail.com"}]
    assert response.status_code ==200
    assert response.json()==data

def test_clientes():
    response = clientes.get("/clientes/1")  
    data =[{"id_cliente":1,"nombre":"Katia","email":"kat160417@gmail.com"}]
    assert response.status_code ==200
    assert response.json()==data