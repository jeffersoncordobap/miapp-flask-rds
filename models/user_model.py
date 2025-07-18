from config.db import conn

def insertar_usuario(nombre, email, foto):
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios (nombre, email, foto_url) VALUES (%s, %s, %s)", (nombre, email, foto))
        conn.commit()