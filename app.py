# app.py
from flask import Flask
from database.conexion import engine, Base
from routes.productos import productos_bp
from routes.contacto import contacto_bp
app = Flask(__name__)

# Crea las tablas si no existen
Base.metadata.create_all(engine)

# Registra las rutas de productos
app.register_blueprint(productos_bp)
app.register_blueprint(contacto_bp)

if __name__ == '__main__':
    app.run(debug=True)
