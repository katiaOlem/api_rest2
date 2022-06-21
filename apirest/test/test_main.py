from fastapi.testclient import TestClient
from code.main import app
clientes = TestClient(app)



def test_index():
    response= clientes.get("/") 
    data = {"message": "API REST"}
    assert response.status_code == 200
    assert response.json() == data



def test_clientes():
    response = clientes.get("/clientes/") 
    data = [{"id_cliente":1,"nombre":"Katia","email":"kat160417@gmail.com"},
    {"id_cliente":2,"nombre":"Itzel","email":"itezel16@gmail.com"},
    {"id_cliente":3,"nombre":"Leo","email":"leo17@gmail.com"}]
    assert response.status_code == 200
    assert response.json() == data

def test_clientes():
    response = clientes.get("/clientes/1") 
    data = [{"id_cliente":1,"nombre":"Katia","email":"kat160417@gmail.com"}]
    assert response.status_code == 200
    assert response.json() == data


def test_clientes_post():
    payload={ "id_cliente": 4, "nombre": "str", "email" : "str"}
    response = clientes.post("/clientes/", json=payload)  
    data = {"message":"Cliente insertado"}
    assert response.status_code ==200
    assert response.json()==data

def test_clientes_update():
    payload={ "id_cliente": 4, "nombre": "Cliente actualizado", "email" : "actualizado@email.com"}
    response = clientes.put("/clientes/", json=payload)
    data = {"message":"Cliente actualizado"}
    assert response.status_code ==200
    assert response.json()==data
    
def test_clientes_delete():
    payload={ "id_cliente": 4, "nombre": "Cliente actualizado", "email" : "actualizado@email.com"}
    response = clientes.delete("/clientes/4", json=payload)
    data = {"message": "Cliente eliminado"}
    assert response.status_code == 200
    assert response.json() == data