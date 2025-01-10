import logging
from logging.handlers import SMTPHandler


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
    
     # Load the configuration from the instance folder
    if app.config.get('TESTING', False):
        app.config.from_pyfile('config-testing.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)
    configure_logging(app)
    # El resto del código
    
    
    app.register_blueprint(public)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    # Custom error handlers
    register_error_handlers(app)
    @login_manager.user_loader
    def load_user(user_id):
        return Users.get_by_id(int(user_id))
    return app
# ///////////////////////////////////////////////////////////////////////////////////////////
def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404
# ///////////////////////////////////////////////////////////////////////////////////////////
def configure_logging(app):
    # Eliminamos los posibles manejadores, si existen, del logger por defecto
    del app.logger.handlers[:]

    # Añadimos el logger por defecto a la lista de loggers
    loggers = [app.logger, logging.getLogger('sqlalchemy')]
    handlers = []

    # Creamos un manejador para escribir los mensajes por consola
    console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.DEBUG) --> desaparece
    console_handler.setFormatter(verbose_formatter())
    # handlers.append(console_handler) --> desaparece
    
    # Verificamos el entorno desde app.config['ENV'] 
    env = app.config.get('ENV', 'production') #'production' como calor predeterminado.
    # if env == 'development' or env == 'testing':
    if env == 'development':
        console_handler.setLevel(logging.DEBUG)
        handlers.append(console_handler)
    elif env == 'testing':
        console_handler.setLevel(logging.INFO)
        handlers.append(console_handler)
    elif env == 'production':
        console_handler.setLevel(logging.INFO)
        handlers.append(console_handler)
        # envio de correo electrónico en caso de error
        mail_handler = SMTPHandler((app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
                            app.config['DONT_REPLY_FROM_EMAIL'],
                            app.config['ADMINS'],
                            '[Error][{}] La aplicación falló'.format(app.config['APP_ENV']),
                            (app.config['MAIL_USERNAME'],
                            app.config['MAIL_PASSWORD']),
                            ())
        mail_handler.setLevel(logging.ERROR)
        mail_handler.setFormatter(mail_handler_formatter())
        handlers.append(mail_handler)
    # Asociamos cada uno de los handlers a cada uno de los loggers
    for l in loggers:
        for handler in handlers:
            l.addHandler(handler)
        l.propagate = False
        l.setLevel(logging.DEBUG)
# ///////////////////////////////////////////////////////////////////////////////////////////
def verbose_formatter():
    return logging.Formatter(
        '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )
# ///////////////////////////////////////////////////////////////////////////////////////////
def mail_handler_formatter():
    return logging.Formatter(
        '''
            Message type:       %(levelname)s
            Location:           %(pathname)s:%(lineno)d
            Module:             %(module)s
            Function:           %(funcName)s
            Time:               %(asctime)s.%(msecs)d

            Message:

            %(message)s
        ''',
        datefmt='%d/%m/%Y %H:%M:%S'
    )
    
