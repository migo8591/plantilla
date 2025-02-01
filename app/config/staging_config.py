from .default import *

from dotenv import load_dotenv
import os

load_dotenv()
user=os.getenv('MYSQL_USER')
password=os.getenv('MYSQL_PASSWORD')
host=os.getenv('MYSQL_HOST')
port=os.getenv('MYSQL_PORT')
database=os.getenv("MYSQL_DATABASE")

# class StagingConfig(Config):
#     SQLALCHEMY_DATABASE_URI= f"mysql://{user}:{password}@{host}:{port}/{database}"
#     ENV="staging"  
DEBUG=False
SQLALCHEMY_DATABASE_URI= f"mysql://{user}:{password}@{host}:{port}/{database}"
# SQLALCHEMY_DATABASE_URI = "sqlite:///blog_educativoII.db"
APP_ENV = APP_ENV_STAGING
