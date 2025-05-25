# Configuracion de SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
#importación de la URI
from config import DATABASE_URI

# crea el motor de la bd usando la URI de Config
#echo=true permite ver en la consola las consultas
engine = create_engine(DATABASE_URI, echo=True)
#ruta dde conexión de a la base dde datos SQLlite utilizada por SQLAlchemy
DATABASE_URI = "sqlite:///database/ferremas.db"
Session = sessionmaker(bind=engine)
Base = declarative_base()
