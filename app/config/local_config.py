from .default import *

DEBUG = True
# SQLALCHEMY_DATABASE_URI = "sqlite:///blog_educativoII.db"
SQLALCHEMY_DATABASE_URI= f"mysql://{user}:{password}@{host}:{port}/{database}"
APP_ENV = APP_ENV_DEVELOPMENT