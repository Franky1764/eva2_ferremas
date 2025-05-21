# scripts/cargar_productos.py
from database.conexion import Session, engine, Base
from models.producto import Producto

# Crea las tablas si no existen
Base.metadata.create_all(engine)
session = Session()

# Elimina productos anteriores (si quieres partir de cero)
session.query(Producto).delete()

# Nuevos productos
productos = [
    Producto(
        codigo="FER123",
        marca="Truper",
        nombre="Taladro percutor 750W",
        modelo="TP-750",
        stock=10,
        precio=45990.0
    ),
    Producto(
        codigo="FER456",
        marca="Bosch",
        nombre="Sierra circular 1400W",
        modelo="SC-1400",
        stock=5,
        precio=78990.0
    ),
    Producto(
        codigo="FER789",
        marca="Makita",
        nombre="Lijadora Orbital 300W",
        modelo="LO-300",
        stock=7,
        precio=64990.0
    ),
    Producto(
        codigo="FER321",
        marca="Stanley",
        nombre="Caja de herramientas 19'' con organizador",
        modelo="CT-19",
        stock=12,
        precio=19990.0
    )
]

session.add_all(productos)
session.commit()
session.close()

print("productos cargados correctamente.")
