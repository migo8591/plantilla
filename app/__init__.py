import logging
from logging.handlers import SMTPHandler
from colorama import Fore, Style, init
from flask import Flask, render_template
from flask_login import LoginManager, current_user
from .public import public
from .auth import auth
from .admin import admin_bp
from extensions import db
from app.auth.models import Users
from flask_migrate import Migrate
from flask_ckeditor import CKEditor # type: ignore
from datetime import timedelta

ckeditor = CKEditor()

init(autoreset=True)
migrate = Migrate()

def create_app(config_class):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    app.config['SESSION_PERMANENT'] = True # Indica que la sesión puede expirar
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)# Tiempo de expiración
    # app.config.from_pyfile('config.py', silent=True)
    if "SQLALCHEMY_DATABASE_URI" not in app.config:
        raise RuntimeError("Falta la configuración de la base de datos (SQLALCHEMY_DATABASE_URI).")
    app.config['CKEDITOR_PKG_TYPE']='full'
    ckeditor.init_app(app)
    
    
     # Load the configuration from the instance folder
    if app.config.get('TESTING', False):
        app.config.from_pyfile('test_config.py', silent=True)
    else:
        app.config.from_pyfile('config.py', silent=True)
    configure_logging(app)
    # El resto del código
    
    
    app.register_blueprint(public)
    app.register_blueprint(auth)
    app.register_blueprint(admin_bp)
    db.init_app(app)
    migrate.init_app(app, db)
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
    print("El entorno es:",app.config['APP_ENV'])
    print("El valor de APP_ENV_PRODUCTION es:",app.config['APP_ENV_PRODUCTION'])
    return app
# //////////////////////////////////////////
def register_error_handlers(app):

    @app.errorhandler(500)
    def base_error_handler(e):
        return render_template('500.html'), 500

    @app.errorhandler(404)
    def error_404_handler(e):
        return render_template('404.html'), 404
    
    @app.errorhandler(401)
    def error_404_handler(e):
        return render_template('401.html'), 401
# -----------------------------
def configure_logging(app):
    
    # Eliminamos los posibles manejadores, si existen, del logger por defecto.
    del app.logger.handlers[:]
    # Añadimos el logger por defecto a la lista de loggers
    loggers = [app.logger,]
    handlers = []
    # Creamos un manejador de consola
    console_handler = logging.StreamHandler()
    # console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(verbose_formatter())
    # handlers.append(console_handler)
    # Asociamos cada uno de los handlers a cada uno de los loggers
    if (app.config['APP_ENV'] == app.config['APP_ENV_LOCAL']) or (app.config['APP_ENV'] == app.config['APP_ENV_TESTING']) or(app.config['APP_ENV']==app.config['APP_ENV_DEVELOPMENT'])or(app.config['APP_ENV']==app.config['APP_ENV_STAGING']):
        console_handler.setLevel(logging.DEBUG)
        handlers.append(console_handler)
    elif app.config['APP_ENV'] == app.config['APP_ENV_PRODUCTION']:
        console_handler.setLevel(logging.INFO)
        handlers.append(console_handler)
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
 

        
    for l in loggers:
        for handler in handlers:
            l.addHandler(handler)
        l.propagate = False
        l.setLevel(logging.DEBUG)
# Diccionario de colores para cada nivel de log
LOG_COLORS = {
    'DEBUG': Fore.BLUE,
    'INFO': Fore.GREEN,
    # 'INFO': Fore.LIGHTRED_EX,
    'WARNING': Fore.YELLOW,
    'ERROR': Fore.RED,
    'CRITICAL': Fore.MAGENTA
}
class ColorFormatter(logging.Formatter):
    """ Formatter personalizado que agrega colores al levelname"""
    def format(self, record):
        levelname_color = LOG_COLORS.get(record.levelname, Fore.WHITE) #Obtiene el color segun el nivel.
        record.levelname = f"{levelname_color}{record.levelname}{Style.RESET_ALL}" #Agrega el color al levelname
        return super().format(record)
def verbose_formatter():
    """Devuelve el formateador con colores"""
    return ColorFormatter(
        # '[%(asctime)s.%(msecs)d]\t %(levelname)s \t[%(name)s.%(funcName)s:%(lineno)d]\t %(message)s',
        # datefmt='%d/%m/%Y %H:%M:%S'
        '[%(asctime)s] %(levelname)s [%(name)s.%(funcName)s:%(lineno)d] %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S'
    )
# --------------------------------------
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
    
# Documentación de Flask sobre logging:   
# https://flask.palletsprojects.com/en/stable/logging/
# https://stackoverflow.com/questions/34274968/how-can-i-email-myself-an-error-log-from-flask