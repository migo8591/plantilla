from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    title_slug = StringField('Título slug', validators=[Length(max=128)])
    content = TextAreaField('Contenido')
    submit = SubmitField('Enviar')
    
class UserAdminForm(FlaskForm):
    is_admin = BooleanField("Administrador")
    submit = SubmitField("Submit")