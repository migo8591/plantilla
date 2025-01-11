from dotenv import load_dotenv
import os

load_dotenv()
user=os.environ['MYSQL_USER']
password=os.environ['MYSQL_PASSWORD']
host=os.environ['MYSQL_HOST']
port=os.environ['MYSQL_PORT']
database=os.environ["MYSQL_DATABASE"]


class Config(object):
    DEBUG = False  # Valor por defecto desactivado
    SECRET_KEY="71110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Configuración del email
    MAIL_SERVER = 'tu servidor smtp'
    MAIL_PORT = 587
    MAIL_USERNAME = 'tu correo'
    MAIL_PASSWORD = 'tu contraseña'
    DONT_REPLY_FROM_EMAIL = 'dirección from'
    ADMINS = ('juanjo@j2logo.com', )
    MAIL_USE_TLS = True
    MAIL_DEBUG = False

class ProductionConfig(Config):
     SQLALCHEMY_DATABASE_URI= f"mysql://{user}:{password}@{host}:{port}/{database}"
     ENV="production"    
class DevelopmentConfig(Config):
    # DEBUG = True  # Activa el modo depuración
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog_educativo.db"
    ENV="development"
class TestingConfig(Config):
    DEBUG = True  # Activa el modo depuración
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog_educativo.db"
    ENV="testing"
    # TESTING=True
    
config = {
    'development': DevelopmentConfig,
    'production':ProductionConfig,
    'testing': TestingConfig
    
}