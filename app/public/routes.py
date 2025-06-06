import logging
from flask import abort, render_template, current_app, request
from . import public
from flask_login import login_required
from app.admin.models import Post
from werkzeug.exceptions import NotFound

from colorama import Fore, Back, Style, init

logger = logging.getLogger(__name__)


@public.route('/')
def home():
    # current_app.logger.info("Posts: %s", posts)
    current_app.logger.info("Mostrando todos los posts")
    logger.info("Showing all posts")
    page = int(request.args.get('page',1))
    per_page = current_app.config['ITEM_PER_PAGE']
    post_pagination = Post.all_paginate(page, per_page)
    return render_template('public/home.html',  post_pagination=post_pagination)

@public.route('/aboutus/')
@login_required
def aboutus():
    return render_template('public/aboutus.html')

@public.route("/post/<string:slug>/")
def show_post(slug):
    print("Showing a post")
    logger.info("Mostrando un post")
    logger.debug("El slug es: %s", slug)
    post = Post.get_by_slug(slug)
    if post is None:
        # logger.info(f"El post con slug {slug} no existe")
        logger.info(print(Fore.GREEN + "El post con slug " + Fore.RED + slug + Fore.GREEN + " no existe...AGUANILE!!!"))
        abort(404)
        # raise NotFound(slug)
    return render_template('public/post_view.html', post=post)

@public.route("/mistake/")
def show_error():
    res = 1 / 0
    posts = Post.get_all()
    logger.info("Resulatdo de la division: %s", res)
    return render_template("public/home.html",posts=posts)
    # abort(500)