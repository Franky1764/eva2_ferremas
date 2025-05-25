from flask import Flask, render_template, request, redirect, url_for
from database.conexion import engine, Base
from routes.productos import productos_bp
from routes.contacto import contacto_bp
from routes.cambio import cambio_bp
from transbank.webpay.webpay_plus.transaction import Transaction
import uuid, json
from services.pago import options
# inicialización de Flask
app = Flask(__name__)
#Rutas de navegación
@app.route('/')
def inicio():
    return render_template('index.html')
@app.route('/contacto-form')
def contacto_form():
    return render_template('contacto.html')
@app.route('/catalogo')
def catalogo():
    return render_template('catalogo.html')
@app.route('/carrito')
def carrito():
    return render_template('carrito.html')
"""
Muestra el resumen del carrito antes de que comience el pago
Recibe el carrito como json desde el formulario
"""
@app.route('/resumen-pago', methods=['POST'])
def resumen_pago():
    carrito = json.loads(request.form.get('carritoData'))
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
    return render_template('resumen_pago.html', carrito=carrito, total=total)
"""
inicia una transacción con webpay plus. Genera la orden y la transacción unica y 
redirige a la plataforma de transbank para el pago.
"""
@app.route('/iniciar-transaccion', methods=['POST'])
def iniciar_transaccion():
    import json
    from flask import redirect, url_for

    carrito = json.loads(request.form.get('carritoData'))
    total = sum(item['precio'] * item['cantidad'] for item in carrito)
#aquí crea los identificadores unicos
    buy_order = 'orden-' + str(uuid.uuid4())[:8]
    session_id = 'session-' + str(uuid.uuid4())[:8]
    return_url = url_for('confirmar_pago', _external=True)
#aquí crea y envia la ttransacción a transbank
    tx = Transaction(options)
    response = tx.create(buy_order, session_id, total, return_url)
#finalmente redirige al formulario de pago.
    return redirect(response['url'] + '?token_ws=' + response['token'])

"""
Esta parte del código confirma si tu transacción fue o no exitosa al volver desde webpay
"""
@app.route('/confirmar-pago', methods=['GET','POST'])
def confirmar_pago():
    token_ws = request.args.get("token_ws") or request.form.get("token_ws")
    if not token_ws:
        return redirect("/rechazo")

    try:
        tx = Transaction(options)
        response = tx.commit(token_ws)
        if response['status'] == 'AUTHORIZED':
            return render_template('exito.html', transaccion=response)
        else:
            return redirect("/rechazo")
    except Exception as e:
        print("Error en confirmación:", e)
        return redirect("/rechazo")

#Vistas del resultaddo del pago
@app.route('/exito')
def pago_exitoso():
    return render_template('exito.html')
@app.route('/rechazo')
def pago_rechazado():
    return render_template('rechazo.html')

# crea las tablas de la base si no existen
Base.metadata.create_all(engine)

# Blueprints
app.register_blueprint(productos_bp)
app.register_blueprint(contacto_bp)
app.register_blueprint(cambio_bp)

#acá ejecutamos la app
if __name__ == '__main__':
    app.run(debug=True)
