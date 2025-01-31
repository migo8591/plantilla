from flask import abort, render_template, url_for, redirect, flash, request
from . import auth
from .forms import SignupForm, LoginForm
from .models import Users
from extensions import db
from urllib.parse import urlparse
from flask_login import current_user, login_user, logout_user
from urllib.parse import urlparse



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
            return render_template('auth/signup.html', form=form, error=error)
        else:
            # Creamos el usuario y lo guardamos
            user= Users(
                nombre=name,
                apellido=lastname,
                correo=email,
                contrasena=password
                )
            print(user.contrasena)
            user.set_password(password)
            print(user.contrasena)
            user.save()
            # Dejamos al usuario logueado
            login_user(user, remember=True)
            next_page = request.args.get('next', None)
            print(f'Next_page = {next_page}')
            if not next_page or urlparse (next_page).netloc != '':
                next_page = urlparse('public.index')
        flash("User added successfully")
        return redirect(url_for("auth.login"))
    return render_template('auth/signup.html', form=form, error=error)




#         if user is not None and user.check_password(form.password.data):
#             login_user(user,remember=form.remember_me.data)
#             next_page = request.args.get('next')
#             if not next_page or urlparse (next_page).netloc != '':
#                 next_page = urlparse('public.index')
#             return redirect(next_page)
#     return render_template("auth/login.html", form=form)
            

@auth.route('/login/', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('public.home'))
    form=LoginForm()
    if form.validate_on_submit():
        user = Users.get_by_email(form.email.data)  
        if user is not None and user.check_password(form.password.data):
            login_user(user,remember=form.remember_me.data)
            next_page = request.args.get('next')
            print(f'Next_page = {next_page}')
            if not next_page or urlparse (next_page).netloc != '':
                print(f'Next_page dentro del if= {next_page}')
                print(f'Next_page dentro del if= {not next_page}')
                next_page = url_for('public.home')
                print(f'Next_page es igual netloc= {next_page}')
            print(f'Next_page = {next_page}')
            print("Login exitoso, no entro al if")
            return redirect(next_page)
    return render_template('auth/login.html', form=form)




@auth.route('/profile/')
def profile():
    return render_template('auth/profile.html')

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))