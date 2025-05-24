# database/conexion.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URI

# config.py
engine = create_engine("sqlite:///database/ferremas.db", echo=True)
DATABASE_URI = "sqlite:///database/ferremas.db"
Session = sessionmaker(bind=engine)
Base = declarative_base()
