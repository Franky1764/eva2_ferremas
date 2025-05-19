# app.py
from database.conexion import engine, Base, Session
from models.producto import Producto

# Crea las tablas
Base.metadata.create_all(engine)

# Insertar productos de ejemplo
session = Session()

producto1 = Producto(
    codigo="FER123",
    marca="Truper",
    nombre="Taladro percutor 750W",
    modelo="TP-750",
    stock=10,
    precio=45990.0
)

producto2 = Producto(
    codigo="FER456",
    marca="Bosch",
    nombre="Sierra circular 1400W",
    modelo="SC-1400",
    stock=5,
    precio=78990.0
)

session.add_all([producto1, producto2])
session.commit()
session.close()

print("Base de datos creada con productos de prueba.")
