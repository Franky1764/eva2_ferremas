# models/producto.py
from sqlalchemy import Column, Integer, String, Float
from database.conexion import Base

class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True)
    codigo = Column(String, nullable=False)
    marca = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    modelo = Column(String)
    stock = Column(Integer)
    precio = Column(Float)

    def __repr__(self):
        return f"<Producto(nombre={self.nombre}, precio={self.precio})>"
