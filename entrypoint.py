from dotenv import load_dotenv
import os
load_dotenv()
from app import create_app

# from app.config import get_config

# configuracion = get_config('development')
# app = create_app(configuracion)
settings_module = os.getenv("APP_SETTINGS_MODULE")
app = create_app(settings_module)   

if __name__ == '__main__':
    app.run()  # Fuerza el modo depuración