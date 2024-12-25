from extensions import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model, UserMixin):
    __tablename__ = 'blog_user'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),  nullable=False)
    apellido= db.Column(db.String(200),  nullable=False)
    correo= db.Column(db.String(200), nullable=False, unique=True)
    contrasena = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    def set_password(self, contrasena):
        self.contrasena = generate_password_hash(contrasena)
    def check_password(self, contrasena):
        return check_password_hash(self.contrasena, contrasena)
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    @staticmethod
    def get_by_id(id):
        return Users.query.get(id)
    @staticmethod
    def get_by_email(correo):
        return Users.query.get(correo)
