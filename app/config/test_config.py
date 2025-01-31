from .base_config import Config

class TestConfig(Config):
    DEBUG=True
    TESTING=True
    SQLALCHEMY_DATABASE_URI = "sqlite:///blog_educativoII.db"
    ENV="development"