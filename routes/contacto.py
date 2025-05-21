from flask import Blueprint, request, jsonify, render_template
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
@contacto_bp.route('/mensajes', methods=['GET'])
def ver_mensajes():
    session = Session()
    mensajes = session.query(Contacto).order_by(Contacto.fecha.desc()).all()
    session.close()
    return render_template('mensajes.html', mensajes=mensajes)

