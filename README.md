# miapp-flask-rds
Aplicación web básica desarrollada con Flask (Python) que permite registrar usuarios (nombre y correo electrónico) y almacenar los datos en una base de datos MySQL RDS alojada en Amazon Web Services (AWS).  La app está preparada para despliegue en una instancia EC2 con Amazon Linux 2023
Para ejecutar este proyecto, necesitas crear un archivo `.env` con tus variables de entorno.

Puedes usar el archivo `.env.example` como plantilla:

1. Copia el archivo `.env.example` y renómbralo a `.env`
2. Llena las variables con tus propias credenciales:

```env
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_NAME=nombre_base_datos
