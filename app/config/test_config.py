# from .default import Config

# class TestConfig(Config):
#     DEBUG=True
#     TESTING=True
#     SQLALCHEMY_DATABASE_URI = "sqlite:///blog_educativoII.db"
#     ENV="development"

from .default import *

DEBUG = True
TESTING = True

ENV="testing"
APP_ENV = APP_ENV_TESTING