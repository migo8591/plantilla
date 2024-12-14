from flask import Flask
from .public import public
from .auth import auth
from .admin import admin

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(public)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    

    return app