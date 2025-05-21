from flask import Flask, render_template, request, redirect, url_for
from database.conexion import engine, Base
from routes.productos import productos_bp
from routes.contacto import contacto_bp
from routes.cambio import cambio_bp
from transbank.webpay.webpay_plus.transaction import Transaction
import uuid, json
from services.pago import options
app = Flask(__name__)

@app.route('/contacto-form')
def contacto_form():
    return render_template('contacto.html')

@app.route('/carrito')
def carrito():
    return render_template('carrito.html')

@app.route('/resumen-pago', methods=['POST'])
def resumen_pago():
    carrito = json.loads(request.form.get('carritoData'))
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    return render_template('resumen_pago.html', carrito=carrito, total=total)

@app.route('/iniciar-transaccion', methods=['POST'])
def iniciar_transaccion():
    import json
    from flask import redirect, url_for

    carrito = json.loads(request.form.get('carritoData'))
    total = sum(item['precio'] * item['cantidad'] for item in carrito)

    buy_order = 'orden-' + str(uuid.uuid4())[:8]
    session_id = 'session-' + str(uuid.uuid4())[:8]
    return_url = url_for('confirmar_pago', _external=True)

    tx = Transaction(options)
    response = tx.create(buy_order, session_id, total, return_url)

    return redirect(response['url'] + '?token_ws=' + response['token'])


@app.route('/confirmar-pago', methods=['GET','POST'])
def confirmar_pago():
    token_ws = request.args.get("token_ws") or request.form.get("token_ws")
    if not token_ws:
        return redirect("/rechazo")

    try:
        tx = Transaction(options)
        response = tx.commit(token_ws)
        if response['status'] == 'AUTHORIZED':
            return redirect("/exito")
        else:
            return redirect("/rechazo")
    except Exception as e:
        print("Error en confirmación:", e)
        return redirect("/rechazo")


@app.route('/exito')
def pago_exitoso():
    return render_template('exito.html')

# Base de datos
Base.metadata.create_all(engine)

# Blueprints
app.register_blueprint(productos_bp)
app.register_blueprint(contacto_bp)
app.register_blueprint(cambio_bp)

if __name__ == '__main__':
    app.run(debug=True)
