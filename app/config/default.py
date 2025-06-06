from os.path import abspath, dirname
from dotenv import load_dotenv
import os
BASE_DIR = dirname(dirname(abspath(__file__)))
SECRET_KEY = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
SQLALCHEMY_TRACK_MODIFICATIONS = False
ITEM_PER_PAGE = 3

load_dotenv()
user=os.getenv('MYSQL_USER')
password=os.getenv('MYSQL_PASSWORD')
host=os.getenv('MYSQL_HOST')
port=os.getenv('MYSQL_PORT')
database=os.getenv("MYSQL_DATABASE")
databaseTest=os.getenv("MYSQL_DATABASE_TEST")

# App environments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
# APP_ENV = ''

# Otros parámetros
...

# Configuración del email
MAIL_SERVER = os.getenv('MY_MYSQL_USER')
MAIL_PORT = os.getenv('MY_MYSQL_USER')
MAIL_USERNAME = os.getenv('MY_MAIL_USERNAME')
MAIL_PASSWORD = os.getenv('MY_MAIL_PASSWORD')
DONT_REPLY_FROM_EMAIL = os.getenv('MY_DONT_REPLY_FROM_EMAIL')
ADMINS = os.getenv('MY_ADMINS ')
MAIL_USE_TLS = os.getenv('MY_MAIL_USE_TLS')
MAIL_DEBUG = os.getenv('MY_MAIL_DEBUG')