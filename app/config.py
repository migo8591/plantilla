class Config:
    DEBUG = False  # Valor por defecto desactivado
    # SECRET_KEY="71110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe"

class DevelopmentConfig(Config):
    DEBUG = True  # Activa el modo depuración
    
config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}