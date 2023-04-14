CREATE TABLE clientes (
  id serial PRIMARY KEY,
  nomb_cliente varchar(50),
  edad int,
  sexo varchar(1)
);
INSERT INTO clientes (nomb_cliente, edad, sexo)
VALUES ('Camilo Andres Puerto', 21, 'M'),
       ('Nancy Camila Torres', 18, 'F'),
       ('Xiomara Cardenas', 22, 'F'),
       ('Pedro Alfonso Peralta', 21, 'M'),
       ('Clara Ines Casallas', 17, 'F');
ALTER TABLE clientes ADD telefono varchar(12);
UPDATE clientes SET telefono = '31055555' WHERE id = 1;
UPDATE clientes SET telefono = '31066666' WHERE id = 2;
UPDATE clientes SET telefono = '31077777' WHERE id = 3;
UPDATE clientes SET telefono = '31088888' WHERE id = 4;
UPDATE clientes SET telefono = '31099999' WHERE id = 5;
ALTER TABLE clientes RENAME COLUMN nomb_cliente TO nombre;
ALTER TABLE clientes RENAME TO cliente;
DELETE FROM cliente WHERE id = 1;
SELECT * FROM cliente;
