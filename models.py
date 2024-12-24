from extensions import db
from datetime import datetime

class Users(db.Model):
    __tablename__ = 'blog_user'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100),  nullable=False)
    apellido= db.Column(db.String(200),  nullable=False)
    correo= db.Column(db.String(200), nullable=False, unique=True)
    contrasena = db.Column(db.String(200), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
