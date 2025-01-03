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

class ProductionConfig(Config):
     SQLALCHEMY_DATABASE_URI= f"mysql://{user}:{password}@{host}:{port}/{database}"
    
class DevelopmentConfig(Config):
    DEBUG = True  # Activa el modo depuración
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog_educativo.db"
class TestingConfig(Config):
    pass
# class TestingConfig(Config):
#     DEBUG = True  # Activa el modo depuración
#     TESTING=True
    
config = {
    'development': DevelopmentConfig,
    'production':ProductionConfig,
    'default': DevelopmentConfig
    
}