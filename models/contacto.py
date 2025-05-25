from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from database.conexion import Base
#modelo ORM que representa el mensaje enviado desde el formulario de contacto
class Contacto(Base):
    __tablename__ = 'contactos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(120), nullable=False)
    mensaje = Column(Text, nullable=False)
    fecha = Column(DateTime, default=datetime.now)
#representación visible del objeto
    def __repr__(self):
        return f"<Contacto(nombre={self.nombre}, correo={self.correo})>"
