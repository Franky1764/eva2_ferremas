from flask import Blueprint, request, jsonify
from models.contacto import Contacto
from database.conexion import Session

contacto_bp = Blueprint('contacto', __name__)

@contacto_bp.route('/contacto', methods=['POST'])
def recibir_contacto():
    datos = request.json
    nombre = datos.get("nombre")
    correo = datos.get("correo")
    mensaje = datos.get("mensaje")

    if not nombre or not correo or not mensaje:
        return jsonify({"error": "Faltan campos obligatorios"}), 400

    session = Session()
    nuevo_contacto = Contacto(nombre=nombre, correo=correo, mensaje=mensaje)
    session.add(nuevo_contacto)
    session.commit()
    session.close()

    return jsonify({"mensaje": "Consulta recibida correctamente"}), 201
