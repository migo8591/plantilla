from app import create_app
from app.config import get_config

configuracion = get_config('development')
app = create_app(configuracion)

if __name__ == '__main__':
    app.run()  # Fuerza el modo depuración