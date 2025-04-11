# from .base_config import Config

# class DevelopmentConfig(Config):
#     DEBUG=True
#     SQLALCHEMY_DATABASE_URI = "sqlite:///blog_educativoII.db"
#     ENV="development"
from .default import *
DEBUG = True
SQLALCHEMY_DATABASE_URI = "sqlite:///blog_educativoII.db"
APP_ENV = APP_ENV_DEVELOPMENT