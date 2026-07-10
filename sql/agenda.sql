CREATE TABLE contactos(
    id_contacto INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    primer_apellido TEXT NOT NULL,
    segundo_apellido TEXT NOT NULL,
    email TEXT NOT NULL,
    telefono TEXT NOT NULL
);

INSERT INTO contactos(nombre,primer_apellido,segundo_apellido,email,telefono)
VALUES
('Dejah','Thoris','Barsonn','dejah@email.com','111111111'),
('Alejandra','Guerra','Mostaza',ale@email.com','444444')',
('Eric','Carrillo','Garcia','eric@email.com','22222222');


SELECT * FROM contactos;