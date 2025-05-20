from flask import Blueprint, jsonify
from services.banco_central import obtener_dolar_actual

cambio_bp = Blueprint('cambio', __name__)

@cambio_bp.route('/valor-dolar', methods=['GET'])
def valor_dolar():
    valor = obtener_dolar_actual()
    if valor:
        return jsonify({"dolar_clp": round(valor, 2)})
    return jsonify({"error": "No se pudo obtener el valor del dólar"}), 500
