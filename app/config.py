class Config(object):
    DEBUG = False  # Valor por defecto desactivado
    SECRET_KEY="71110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe"

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql://root:op3ra_4Repo2024@localhost:3306/blogeducativo506"
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
    'production':DevelopmentConfig,
    'default': DevelopmentConfig
    
}