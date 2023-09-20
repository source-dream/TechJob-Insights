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
