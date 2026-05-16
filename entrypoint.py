from dotenv import load_dotenv
import os
load_dotenv()
from app import create_app
from flask import send_from_directory

# from app.config import get_config

# configuracion = get_config('development')
# app = create_app(configuracion)
settings_module = os.getenv("APP_SETTINGS_MODULE")
app = create_app(settings_module)   

@app.route("/media/posts/<filename>")
def media_posts(filename):
    dir_path = os.path.join(
        app.config['MEDIA_DIR'],
        app.config['POSTS_IMAGES_DIR'])
    return send_from_directory(dir_path, filename)

settings_module = os.getenv("APP_SETTINGS_MODULE")
if __name__ == '__main__':
    app.run()  # Fuerza el modo depuración