import logging
from colorama import Fore
from flask import abort, render_template, url_for, redirect
from . import admin_bp
from app.auth.models import Users
from .forms import PostForm, UserAdminForm
from app.admin.models import Post
from flask_login import current_user, login_required
from app.auth.decorators import admin_required

logger = logging.getLogger(__name__)

@admin_bp.route("/index/")
@login_required
@admin_required
def adminIndex():
    return render_template("admin/admin.html")
    

@admin_bp.route("/admin-posts")  
@login_required
def list_posts():
    post=Post.get_all()
    return render_template("admin/admin-posts.html", posts=post) 

@admin_bp.route("/post/", methods=['GET','POST'], defaults={'post_id':None})
@login_required
def postform(post_id):
    # if current_user.is_authenticated:
    # print("El usuario está autenticado", current_user)
    # print("La url es: ",url_for('admin.postform', post_id=10, slug="leccion-1",time="1.5"))
    # print("La url es: ",url_for('admin.postform', post_id=post_id, slug=slug))
    form = PostForm()
    if form.validate_on_submit():
        titulo = form.title.data
        titulo_slug = form.title_slug.data
        contenido = form.content.data
        print("Formulario validado", titulo,  contenido)
        post = Post(user_id=current_user.id,title=titulo, title_slug=titulo_slug,content=contenido,)
        print("post.id debe ser None =", post.id)
        post.save()
        print("post.id no debe ser None ya que si se guardo =", post.id)
        return redirect(url_for('public.home'))
    return render_template('admin/postForm.html', form=form)

@admin_bp.route("/post-view/<int:post_id>/")
def view_post(post_id):
    post=Post.get_by_id(post_id)
    logger.info(f"Mostrando el post {post.title}")
    if post is None:
        logger.info(f"El post no {post_id} existe")
        abort(404)
    return render_template("admin/admin-post-view.html", post=post)
@admin_bp.route("/post/<int:post_id>/", methods=['GET','POST'])
def editPost(post_id):
    post=Post.get_by_id(post_id)
    if post is None:
        logger.info(f'El post {Fore.RED}{post_id}{Fore.RESET} no existe')
        abort(404)
    form = PostForm(obj=post)
    if form.validate_on_submit():
        #Actualiza los campos del post existente
        post.title = form.title.data
        post.content= form.content.data
        post.save()
        logger.info(f'{Fore.YELLOW} Editando el post numero{Fore.RESET} {Fore.RED}{post_id}{Fore.RESET}')
        return redirect(url_for("public.home"))
    return render_template("admin/postForm.html", form=form, post=editPost)


@admin_bp.route("/post/delete/<int:post_id>/")
@login_required
@admin_required
def delete_post(post_id):
    logger.info(f'{Fore.YELLOW}Se va a eliminar el post #{Fore.RESET} {Fore.RED}{post_id}{Fore.RESET}')
    post=Post.get_by_id(post_id)
    if post is None:
        logger.info(f'{Fore.YELLOW}Se va a eliminar el post #{Fore.RESET} {Fore.RED}{post_id}{Fore.RESET}')
        abort(404)
    post.delete()
    logger.info(f'{Fore.YELLOW}El post{Fore.RESET} {Fore.RED}{post.title}{Fore.RESET}')
    return redirect(url_for('admin.list_posts'))

# --------------------- Users --------------------------#
@admin_bp.route('/users/')
@login_required
@admin_required
def users():
    our_users = (Users.query.order_by(Users.date_added))
    return render_template('admin/users.html', usuarios = our_users)

@admin_bp.route("/user/<int:user_id>/", methods=["GET","POST"])
@login_required
def updateUserForm(user_id):
    user = Users.get_by_id(user_id)
    form = UserAdminForm(obj=user)
    if user is None:
        logger.info(f'El usuario {user_id} no existe')
        abort(404)
    if form.validate_on_submit():
        user.is_admin = form.is_admin.data
        user.save()
        logger.info(print(Fore.GREEN + "Save the user " + Fore.RED + str(user_id)+ Fore.RESET))
        return redirect(url_for("admin.users"))
    return render_template("admin/userForm.html", form=form, usuario=user)