Cual error tengo si utilizo mysql en los siguientes entornos:
app/admin/models.py
from slugify import slugify
from flask import url_for
from extensions import db
from sqlalchemy.exc import IntegrityError
from colorama import Fore, Back, Style, init
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    title_slug = db.Column(db.String(256), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<Post: {self.title}>"
    def save(self):
        if not self.id:
            db.session.add(self)
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        saved = False
        print(Fore.YELLOW +"1. Valor de saved", saved)
        print(Fore.YELLOW +"2. Valor de not saved", not saved)
        count = 0
        while not saved:
            print(Fore.LIGHTBLUE_EX +"(2.5). Valor de title_slug es:"+ Fore.RED + self.title_slug)
            try:
                print(Fore.GREEN +"3.Intentando guardar el slug")
                print(Fore.YELLOW +"(5.1). Valo de self id es: " + Fore.RED + str(self.id))
                print(f"Intentando guardar: title_slug='{self.title_slug}'")
                db.session.commit()
                saved = True
                if saved == True:
                    print(Fore.GREEN +"7. end of the loop")
            except IntegrityError:
                print(Fore.GREEN + "4. Valor de saved es false xq no se logro guardar: " + Fore.RED + str(saved) + Fore.GREEN + ". Efectivamente lo es")
                print(Fore.RED +"5. Ocurrio un error de integridad")
                print(Fore.YELLOW +"(5.1). Valo de self id es: " + Fore.RED + str(self.id))
                db.session.rollback()
                print(Fore.YELLOW +"(5.2). Valo de self id es: " + Fore.RED + str(self.id))
                print(Fore.YELLOW +"6. Deshace la transacción y entra otra vez al while", Fore.RED + str(saved))
                count += 1
                self.title_slug = f"{slugify(self.title)}-{count}"
                if not self.id:
                    db.session.add(self)
    def public_url(self):
        return url_for('public.show_post', slug=self.title_slug)
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    @staticmethod
    def get_by_slug(slug):
        return Post.query.filter_by(title_slug=slug).first()
    @staticmethod
    def get_all():
        return Post.query.all()
    @staticmethod
    def get_by_id(id):
        return Post.query.get(id)
    
app/auth/models.py
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
    is_admin = db.Column(db.Boolean, default=False)
    posts=db.relationship('Post', backref='user')
    
    
    def set_password(self, contrasena):
        self.contrasena = generate_password_hash(contrasena)
    def check_password(self, contrasena):
        return check_password_hash(self.contrasena, contrasena)
    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    @staticmethod
    def get_all():
        return Users.query.all()
    @staticmethod
    def get_by_id(id):
        return Users.query.get(id)
    @staticmethod
    def get_by_email(correo):
        # return Users.query.get(correo)
        return Users.query.filter_by(correo=correo).first()

https://chatgpt.com/share/679dfdb1-3e4c-800d-85cd-4c8758f65ffd