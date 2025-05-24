BEGIN TRANSACTION;
CREATE TABLE productos (
	id INTEGER NOT NULL, 
	codigo VARCHAR NOT NULL, 
	marca VARCHAR NOT NULL, 
	nombre VARCHAR NOT NULL, 
	modelo VARCHAR, 
	stock INTEGER, 
	precio FLOAT, 
	PRIMARY KEY (id)
);
INSERT INTO "productos" VALUES(1,'FER123','Truper','Taladro percutor 750W','TP-750',10,45990.0);
INSERT INTO "productos" VALUES(2,'FER456','Bosch','Sierra circular 1400W','SC-1400',5,78990.0);
INSERT INTO "productos" VALUES(3,'FER789','Makita','Lijadora Orbital 300W','LO-300',7,64990.0);
INSERT INTO "productos" VALUES(4,'FER321','Stanley','Caja de herramientas 19'''' con organizador','CT-19',12,19990.0);
COMMIT;
