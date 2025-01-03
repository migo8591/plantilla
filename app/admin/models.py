from slugify import slugify
from flask import url_for
from extensions import db
from sqlalchemy.exc import IntegrityError

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    # user_id = db.relationship('User', back_populates='posts')
    user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    title_slug = db.Column(db.String(256), nullable=False, unique=True)
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"<Post: {self.title}>"
   

    def save(self):
        if not self.id:
            db.session.add(self)
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                db.session.rollback()
                count += 1
                self.title_slug = f"{slugify(self.title)}-{count}"

    def public_url(self):
        return url_for('show_post', slug=self.title_slug)

    @staticmethod
    def get_by_slug(slug):
        return Post.query.filter_by(slug=slug).first()

    @staticmethod
    def get_all():
        return Post.query.all()