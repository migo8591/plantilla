from flask import abort, render_template
from . import auth


@auth.route('/signup/')
def signup():
    return render_template('auth/signup.html')

@auth.route('/login/')
def login():
    return render_template('auth/login.html')