# database/conexion.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URI

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
