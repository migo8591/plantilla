from flask import Flask
from flask_login import LoginManager, current_user
from .public import public
from .auth import auth
from .admin import admin
from extensions import db
from app.auth.models import Users

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(public)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    @login_manager.user_loader
    def load_user(user_id):
        return Users.get_by_id(int(user_id))

    

    return app