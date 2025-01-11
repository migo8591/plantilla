from app import create_app
from app.config import config

app = create_app(config['development'])
