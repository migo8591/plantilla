from flask import Flask
from .public import public
from .auth import auth
from .admin import admin
from extensions import db

def create_app(config_class):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog_educativo.db"
    app.config.from_object(config_class)
    app.register_blueprint(public)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    

    return app