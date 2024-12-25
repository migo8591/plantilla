from flask import abort, render_template, url_for, redirect, flash, request
from . import auth
from .forms import SignupForm
from models import Users
from extensions import db
from urllib.parse import urlparse
from flask_login import current_user, login_user, logout_user


@auth.route('/signup/', methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('public.home'))
    form = SignupForm()
    error = None 
    if form.validate_on_submit():
        name=form.name.data
        lastname=form.lastname.data
        email=form.email.data
        password=form.password.data
        # Comprobamos que no hay ya un usuario con ese email
        user = Users.get_by_email(email)
        if user is not None:
            error = f"El email {email} ya está en uso"
        else:
            # Creamos el usuario y lo guardamos
            user= Users(
                nombre=name,
                apellido=lastname,
                correo=email,
                contrasena=password
                )
            user.set_password(password)
            user.save()
            # Dejamos al usuario logueado
            login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or urlparse (next_page).netloc != '':
                next_page = urlparse('public.index')
        flash("User added successfully")
        return redirect(url_for("auth.login"))
    return render_template('auth/signup.html', form=form, error=error)

@auth.route('/login/')
def login():
    return render_template('auth/login.html')

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))