from flask import abort, render_template, url_for, redirect, flash
from . import auth
from .forms import SignupForm
from models import Users
from extensions import db


@auth.route('/signup/', methods=['GET','POST'])
def signup():
    form = SignupForm()
    error = None 
    if form.validate_on_submit():
        user = Users.query.filter_by(correo = form.email.data).first()
        if user is None:
            user= Users(
                nombre=form.name.data,
                apellido=form.lastname.data,
                correo=form.email.data,
                contrasena=form.password.data)
            db.session.add(user)
            db.session.commit()
        flash("User added successfully")
        name = form.name.data
        namels = form.name.data
        email = form.email.data
        password = form.password.data
        print(f'name: {name}, apellido: {namels} email: {email} y password: {password}')
        form.name.data=""
        form.email.data=""
        form.password.data=""
        return redirect(url_for("auth.login"))
    return render_template('auth/signup.html', form=form, error=error)

@auth.route('/login/')
def login():
    return render_template('auth/login.html')