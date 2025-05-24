import unittest
from app import create_app, db
from app.auth.models import Users


class BaseTestClass(unittest.TestCase):
    def setUp(self):
        self.app = create_app("app.config.test_config")
        self.client = self.app.test_client()
        # Crea un contexto de aplicación:
        with self.app.app_context():
            #Crea las tablas de la base de datos:
            db.create_all()
            #Creamos un usuario administrador:
            BaseTestClass.create_user('admin','munoz', 'admin@xyz.com', '1111', True)
            #Creamos un usuario invitado:
            BaseTestClass.create_user('guest','fanny','guest@xyz.com', '2222', False)
    def tearDown(self): 
        with self.app.app_context():
            # Elimina todas las tablas de la base de datos:
            db.session.remove()
            db.drop_all()       
            
    @staticmethod
    def create_user(nombre,apellido,correo, contrasena, is_admin):
        user = Users()
        user.nombre = nombre
        user.apellido = apellido
        user.correo = correo
        user.set_password(contrasena)
        user.is_admin = is_admin
        user.save()
        return user
    
    
# This is a base test case class for setting up and tearing down the test environment.
# It initializes the Flask application and the database for testing purposes. (facilitado por copilot )
# classtCase(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app('testing')
#         self.app_context = self.app.app_context()
#         self.app_context.push()
#         db.create_all()

#     def tearDown(self):
#         db.session.remove()
#         db.drop_all()
#         self.app_context.pop()


# https://chatgpt.com/share/67fbb772-1e98-800d-8b34-55a2ed5d6802