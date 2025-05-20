# routes/productos.py
from flask import Blueprint, jsonify
from models.producto import Producto
from database.conexion import Session

productos_bp = Blueprint('productos', __name__)


@productos_bp.route('/productos', methods=['GET'])
def obtener_productos():
    """
    Devuelve una lista de todos los productos disponibles en la base de datos.
    """
    session = Session()
    productos = session.query(Producto).all()

    lista = []
    for p in productos:
        lista.append({
            "id": p.id,
            "codigo": p.codigo,
            "marca": p.marca,
            "nombre": p.nombre,
            "modelo": p.modelo,
            "stock": p.stock,
            "precio": p.precio
        })

    session.close()
    return jsonify(lista)

@productos_bp.route('/productos/<int:producto_id>', methods=['GET'])
def obtener_producto_por_id(producto_id):
    """
    Devuelve los detalles de un producto específico por su ID.
    """
    session = Session()
    producto = session.query(Producto).get(producto_id)

    if not producto:
        session.close()
        return jsonify({"error": "Producto no encontrado"}), 404

    resultado = {
        "id": producto.id,
        "codigo": producto.codigo,
        "marca": producto.marca,
        "nombre": producto.nombre,
        "modelo": producto.modelo,
        "stock": producto.stock,
        "precio": producto.precio
    }

    session.close()
    return jsonify(resultado)
