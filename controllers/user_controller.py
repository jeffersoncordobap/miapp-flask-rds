from models.user_model import insertar_usuario

def guardar_usuario(nombre, email):
    insertar_usuario(nombre, email)