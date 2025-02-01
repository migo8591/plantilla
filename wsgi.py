from dotenv import load_dotenv
import os
load_dotenv()
from app import create_app


# app = create_app(config['development'])
settings_module = os.getenv("APP_SETTINGS_MODULE")
app = create_app(settings_module)   

