from flask import abort, render_template, current_app
from . import public
from flask_login import login_required
from app.admin.models import Post
from werkzeug.exceptions import NotFound


@public.route('/')
def home():
    posts = Post.get_all()
    # current_app.logger.info("Posts: %s", posts)
    current_app.logger.info("Mostrando todos los posts")
    return render_template('public/home.html', posts=posts)

@public.route('/aboutus/')
@login_required
def aboutus():
    return render_template('public/aboutus.html')

@public.route("/<string:slug>/")
def show_post(slug):
    post = Post.get_by_slug(slug)
    if post is None:
        # abort(404)
        raise NotFound(slug)
    return render_template('public/post_view.html', post=post)

@public.route("/error")
def show_error():
    res = 1 / 0
    # posts = Post.get_all()
    return render_template("public/index.html")