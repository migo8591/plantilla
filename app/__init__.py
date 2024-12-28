from flask import Flask, render_template
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
    def register_error_handlers(app):

        @app.errorhandler(500)
        def base_error_handler(e):
            return render_template('500.html'), 500

        @app.errorhandler(404)
        def error_404_handler(e):
            return render_template('404.html'), 404
    @login_manager.user_loader
    def load_user(user_id):
        return Users.get_by_id(int(user_id))
    # Custom error handlers
    register_error_handlers(app)
    return app