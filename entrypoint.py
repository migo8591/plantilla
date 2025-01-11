from app import create_app
from app.config import config

configuracion = config['production']
app = create_app(configuracion)

if __name__ == '__main__':
    app.run()  # Fuerza el modo depuración