from flask import render_template, redirect, url_for, jsonify
from . import admin_bp
from flask_login import current_user
from app.models import User
from app import db

@admin_bp.route("/")
def admin():
    if current_user.is_authenticated and current_user.is_admin:
        return render_template('admin.html')
    return redirect(url_for('login'))

@admin_bp.route("/data")
def admin_data():
    if current_user.is_authenticated and current_user.is_admin:
        return render_template('admin-data.html')
    return redirect(url_for('login'))

@admin_bp.route("/user")
def admin_user():
    if current_user.is_authenticated and current_user.is_admin:
        users = User.query.all()
        return render_template('admin-user.html', users=users)
    return redirect(url_for('login'))

@admin_bp.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    if current_user.is_authenticated and current_user.is_admin:
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'})
        else:
            return jsonify({'message': 'User not found'}), 404