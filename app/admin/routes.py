from flask import abort, render_template
from . import admin


@admin.route('/users/')
def home():
    return render_template('admin/users.html')