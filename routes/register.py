from flask import Blueprint, request, redirect, render_template
from controllers.user_controller import guardar_usuario
from config.s3 import subir_a_s3

register_bp = Blueprint('register', __name__)

@register_bp.route('/')
def index():
    return render_template('index.html')

@register_bp.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    email = request.form['email']
    
    # Manejo del archivo
    foto = request.files['foto']
    foto_url = subir_a_s3(foto) if foto else None

    guardar_usuario(nombre, email, foto_url)
    return redirect('/')
