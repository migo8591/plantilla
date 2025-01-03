from flask import abort, render_template, url_for, redirect
from . import admin
from app.auth.models import Users
from .forms import PostForm
from app.admin.models import Post
from flask_login import current_user



@admin.route('/users/')
def users():
    our_users = (Users.query.order_by(Users.date_added))
    return render_template('admin/users.html', usuarios = our_users)

@admin.route("/post/", methods=['GET','POST'], defaults={'post_id':None})
@admin.route("/post/<int:post_id>/", methods=['GET','POST'])
def postform(post_id):
    # print("La url es: ",url_for('admin.postform', post_id=10, slug="leccion-1",time="1.5"))
    # print("La url es: ",url_for('admin.postform', post_id=post_id, slug=slug))
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        # title_slug = form.title_slug.data
        content = form.content.data
        # print("Formulario validado", title, title_slug, content)
        post = Post(user_id=current_user,title=title, content=content)
        return redirect(url_for('public.home'))
    return render_template('admin/post.html', form=form)