from flask import abort, render_template
from . import admin


@admin.route('/users/')
def users():
    return render_template('admin/users.html')