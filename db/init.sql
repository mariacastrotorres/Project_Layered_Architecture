CREATE TABLE persona  (
	id SERIAL NOT NULL,
	nombre VARCHAR(50),
	apellido VARCHAR(50),
	imagen VARCHAR(500),
	PRIMARY KEY (id)
);

CREATE TABLE mascota  (
	id SERIAL NOT NULL,
    id_persona INTEGER (),
	nombre VARCHAR(50),
    PRIMARY KEY (id)
);