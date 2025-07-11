from flask import Blueprint, request, render_template
from controllers.user_controller import guardar_usuario

register_bp = Blueprint('register', __name__)

@register_bp.route('/')
def index():
    return render_template('index.html')

@register_bp.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    email = request.form['email']
    guardar_usuario(nombre, email)
    return "¡Datos guardados exitosamente!"