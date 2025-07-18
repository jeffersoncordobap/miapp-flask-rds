from flask import Flask
from routes.register import register_bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.register_blueprint(register_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)