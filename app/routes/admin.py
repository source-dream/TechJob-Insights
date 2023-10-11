<<<<<<< HEAD
from flask import render_template, redirect, url_for, jsonify
from . import admin_bp
from flask_login import current_user
from app.models import User, Job, PageVisit
from app import db
import pandas as pd
from datetime import date
import datetime
import plotly.express as px

@admin_bp.route("/")
def admin():
    if current_user.is_authenticated and current_user.is_admin:
        job_size = len(Job.query.all())
        user_size = len(User.query.all())
        visit_time = 0
        visit_time_day = 0
        hourly_visits = [0] * 24
        current_date = date.today()
        visits = PageVisit.query.all()
        for visit in visits:
            visit_time += visit.count 
            if visit.timestamp.date() == current_date:
                hour = visit.timestamp.hour
                visit_time_day += visit.count
                hourly_visits[hour] += visit.count
        fig = px.line(x=range(24), y=hourly_visits, title='当天每个小时的访问量')
        fig.update_layout(
            autosize=False,
            height=600,
            width=1280,
        )
        graph_html = fig.to_html(full_html=False, config={'displayModeBar': False})
        return render_template('admin.html',job_size=job_size, user_size=user_size, graph_html=graph_html, visit_time=visit_time, visit_time_day=visit_time_day)
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
=======
from flask import render_template, redirect, url_for
from app.routes import admin_bp
from app.models import User

# 示例用户数据
users = [
    User(id=1, username='admin', email='admin@example.com'),
    User(id=2, username='user1', email='user1@example.com'),
    User(id=3, username='user2', email='user2@example.com'),
]

# 后台账号信息管理页面
@admin_bp.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html', users=users)

# 编辑用户页面
@admin_bp.route('/admin/edit_user/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    # 根据用户ID查找用户
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        # 如果用户不存在，可以返回一个错误页面或重定向到管理页面
        return redirect(url_for('admin.admin'))

    # 处理编辑用户的表单提交
    if request.method == 'POST':
        # 在这里处理编辑用户的逻辑
        pass  # 你可以根据需要添加具体的编辑逻辑

    return render_template('edit_user.html', user=user)

# 删除用户
@admin_bp.route('/admin/delete_user/<int:user_id>', methods=['GET'])
def delete_user(user_id):
    # 在这里处理删除用户的逻辑
    user_to_delete = next((user for user in users if user.id == user_id), None)
    if user_to_delete:
        users.remove(user_to_delete)

    return redirect(url_for('admin.admin'))

# 添加用户页面
@admin_bp.route('/admin/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # 在这里处理添加用户的逻辑
        pass  # 你可以根据需要添加具体的添加逻辑

    return render_template('add_user.html')

# 其他管理操作可以继续添加
>>>>>>> 4030101f55c1ee59ee26e71b73bb56b575fc754b
