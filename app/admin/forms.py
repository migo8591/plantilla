from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length
from flask_ckeditor import CKEditorField

class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=128)])
    title_slug = StringField('Título slug', validators=[Length(max=128)])
    # content = TextAreaField('Contenido')
    content = CKEditorField('Content', validators=[DataRequired()])
    submit = SubmitField('Enviar')
    
class UserAdminForm(FlaskForm):
    is_admin = BooleanField("Administrador")
    submit = SubmitField("Submit")