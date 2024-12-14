from flask import abort, render_template
from . import public


@public.route('/')
def home():
    return render_template('public/home.html', num_posts=0)

@public.route('/aboutus/')
def aboutus():
    return render_template('public/aboutus.html')