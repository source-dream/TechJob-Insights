from flask import render_template, redirect, url_for, jsonify
from . import admin_bp
from app.models import User
from app import db

@admin_bp.route("/")
def admin():
    return render_template('admin.html')

@admin_bp.route("/data")
def admin_data():
    return render_template('admin-data.html')

@admin_bp.route("/user")
def admin_user():
    users = User.query.all()
    return render_template('admin-user.html', users=users)

@admin_bp.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    else:
        return jsonify({'message': 'User not found'}), 404