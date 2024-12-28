from flask import abort, render_template
from . import public
from flask_login import login_required


@public.route('/')
def home():
    return render_template('public/home.html', num_posts=0)

@public.route('/aboutus/')
@login_required
def aboutus():
    return render_template('public/aboutus.html')

@public.route("/error")
def show_error():
    res = 1 / 0
    # posts = Post.get_all()
    return render_template("public/index.html")