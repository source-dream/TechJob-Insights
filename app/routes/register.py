from flask import request, render_template, flash, url_for, redirect
from sqlalchemy.testing import db
from werkzeug.security import generate_password_hash

from app import app
from app.models import User

# 注册页面
# 注册验证，注册功能实现，注册成功后跳转到登录页面
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if is_null(username, password):
            login_massage = "账号和密码是必填！"
            return render_template('register.html', message=login_massage)
        elif exist_user(username):
            login_massage = "用户已存在，请直接登录！"
            return render_template('register.html', message=login_massage)
        else:
            hashed_password = generate_password_hash(password, method='sha256')
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('注册成功，请登录', 'success')
            return redirect(url_for('login'))

    # 如果是GET请求或者注册失败，渲染注册页面
    return render_template('register.html')

# 判断用户是否存在
def exist_user(username):
    user = User.query.filter_by(username=username).first()
    return user is not None

# 判断账号和密码是否为空
def is_null(username, password):
    return username.strip() == '' or password.strip() == ''
