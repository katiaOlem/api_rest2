DROP TABLE IF EXISTS clientes;
CREATE TABLE  clientes(
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT, 
    nombre varchar(50) NOT NULL,
    email varchar(50) NOT NULL);

INSERT INTO clientes(nombre,email) VALUES("Katia","kat160417@gmail.com");
INSERT INTO clientes(nombre,email) VALUES("Itzel","itezel16@gmail.com");
INSERT INTO clientes(nombre,email) VALUES("Leo","leo17@gmail.com");

.headers ON

SELECT *FROM clientes;