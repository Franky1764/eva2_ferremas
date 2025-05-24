from database.conexion import engine
import sqlite3

# Ruta del archivo de base de datos usado por SQLAlchemy
db_path = "database/ferremas.db"

# Conexión directa con sqlite3
conn = sqlite3.connect(db_path)


with open("ferremas.sql", "w", encoding="utf-8") as f:
    for line in conn.iterdump():
        f.write(f"{line}\n")

conn.close()
print("Exportación completada: ferremas.sql")
