from flask import render_template, request, session, flash, url_for, redirect
from werkzeug.security import check_password_hash

from app import app
from app.models import User

#登录验证,登录功能实现
@app.route('/login')
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username = username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            flash('登录成功', 'success')
            return redirect(url_for('user_profile'))
        else:
            flash('账号或密码错误')
    return render_template('login.html')