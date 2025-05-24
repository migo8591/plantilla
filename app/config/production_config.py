# from .default import Config

# from dotenv import load_dotenv
# import os

# load_dotenv()
# user=os.environ['MYSQL_USER']
# password=os.environ['MYSQL_PASSWORD']
# host=os.environ['MYSQL_HOST']
# port=os.environ['MYSQL_PORT']
# database=os.environ["MYSQL_DATABASE"]

# class ProductionConfig(Config):
#     SQLALCHEMY_DATABASE_URI= f"mysql://{user}:{password}@{host}:{port}/{database}"
#     ENV="production"  
from .default import *

DEBUG = False

APP_ENV = APP_ENV_PRODUCTION
SQLALCHEMY_DATABASE_URI= f"mysql://{user}:{password}@{host}:{port}/{database}"
# ENV="production"