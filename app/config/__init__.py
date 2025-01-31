from .dev_config import DevelopmentConfig
from .production_config import ProductionConfig
from .staging_config import StagingConfig
from .test_config import TestConfig

configuration = {
    'default': DevelopmentConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'staging': StagingConfig,
    'testing': TestConfig,
}
def get_config(env_name):
    return configuration.get(env_name, configuration['default'])