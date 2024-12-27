from flask import abort, render_template
from . import admin
from app.auth.models import Users


@admin.route('/users/')
def users():
    our_users = (Users.query.order_by(Users.date_added))
    return render_template('admin/users.html', usuarios = our_users)