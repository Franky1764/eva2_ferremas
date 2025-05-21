# 🔧 FERREMAS - Proyecto de Integración de Plataformas

Este proyecto corresponde a la segunda etapa del proyecto semestral para la empresa ficticia **FERREMAS**, orientado a la integración de servicios, creación de APIs REST y simulación de un flujo de compra completo utilizando Webpay Plus.

## 🧰 Funcionalidades

- Consulta de productos: código, marca, modelo, precio y stock.
- Carrito de compras funcional con almacenamiento en localStorage.
- Conversión de moneda en tiempo real usando la API del Banco Central de Chile.
- Formulario de contacto con almacenamiento en base de datos.
- Integración completa de Webpay Plus (entorno de pruebas):
  - Resumen de compra
  - Redirección a Webpay
  - Confirmación de transacción
  - Mensajes de éxito o rechazo

## ⚙️ Tecnologías

- Backend: Python + Flask
- Frontend: HTML + Bootstrap + JS puro
- Base de datos: SQLite + SQLAlchemy
- APIs externas:
  - [Banco Central de Chile](https://si3.bcentral.cl)
  - [Webpay Plus (Transbank Sandbox)](https://www.transbankdevelopers.cl)

## 🚀 Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tuusuario/eva2_ferremas.git
   cd eva2_ferremas

2. Crear entorno virtual e instalar dependencias:
```bash
  python -m venv .venv
  source .venv/Scripts/activate  # Windows
  pip install -r requirements.txt
```
3. Agregar archivo credenciales.txt con tus datos del Banco Central:
```css
    usuario@ejemplo.com

    contraseñaSuperSegura
```
4. Ejecutar el script de carga de productos:
```bash
  python -m scripts.cargar_productos
```
5. Iniciar la aplicación:
```bash
    python app.py
```
6. Acceder a la aplicación:

    http://127.0.0.1:5000

## 🧪 Pruebas

    Puedes acceder a los endpoints /productos, /contacto, /valor-dolar, y /mensajes.

    Todo el flujo de compra puede simularse en modo local y validarse visualmente.

## 📁 Estructura del proyecto
```pgsql
eva2_ferremas/
├── app.py
├── templates/
│   ├── index.html
│   ├── carrito.html
│   ├── resumen_pago.html
│   ├── exito.html
│   ├── contacto.html
│   ├── mensajes.html
│   └── catalogo.html
├── static/
├── routes/
│   ├── productos.py
│   ├── contacto.py
│   └── cambio.py
├── services/
│   ├── banco_central.py
│   └── pago.py
├── database/
│   └── conexion.py
├── models/
│   ├── producto.py
│   └── contacto.py
└── scripts/
    └── cargar_productos.py
```
## ✅ Estado del proyecto

✔️ Implementación terminada
✔️ Webpay integrado en entorno de prueba
✔️ Conversión monetaria funcionando
✔️ Documentación finalizada
✔️ Entrega lista para evaluación ✨

### 📅 Última actualización: 21 de mayo de 2025
### 💻 Desarrollado por: Daniela Castillo / Auraria✨