from .default import *



# class StagingConfig(Config):
#     SQLALCHEMY_DATABASE_URI= f"mysql://{user}:{password}@{host}:{port}/{database}"
#     ENV="staging"  
DEBUG=False
SQLALCHEMY_DATABASE_URI= f"mysql://{user}:{password}@{host}:{port}/{database}"
# SQLALCHEMY_DATABASE_URI = "sqlite:///blog_educativoII.db"
APP_ENV = APP_ENV_STAGING
