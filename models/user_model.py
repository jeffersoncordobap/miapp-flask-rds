from config.db import conn

def insertar_usuario(nombre, email):
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios (nombre, email) VALUES (%s, %s)", (nombre, email))
        conn.commit()