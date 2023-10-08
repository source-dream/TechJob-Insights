from flask import render_template, redirect, url_for
from . import admin_bp
from app.models import User

@admin_bp.route("/")
def admin():
    return render_template('admin.html')

@admin_bp.route("/data")
def admin_data():
    return render_template('admin-data.html')

@admin_bp.route("/user")
def admin_user():
    return render_template('admin-user.html')