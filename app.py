# app.py
from flask import Flask, render_template
from database.conexion import engine, Base
from routes.productos import productos_bp
from routes.contacto import contacto_bp
from routes.cambio import cambio_bp
app = Flask(__name__)
@app.route('/contacto-form')
def contacto_form():
    return render_template('contacto.html')
@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

# Crea las tablas si no existen
Base.metadata.create_all(engine)

# Registra las rutas de productos
app.register_blueprint(productos_bp)
app.register_blueprint(contacto_bp)
app.register_blueprint(cambio_bp)

if __name__ == '__main__':
    app.run(debug=True)
