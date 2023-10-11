<<<<<<< HEAD
from flask import render_template, request, url_for, flash, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app.models import User
from flask_login import login_user, logout_user, current_user

@app.route('/login', methods=['GET', 'POST'])
def login():
    next_page = session.pop('next', None)
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user is None or not user.check_password(request.form['password']):
            flash('Invalid email or password', 'error')
            return redirect(url_for('login'))
        login_user(user, remember=True)
        # login_user(user, remember=request.form['remember_me'])
        if current_user.is_admin:
            return redirect(url_for('admin.admin'))
        return redirect(next_page or url_for('index.index'))
    if current_user.is_authenticated:
        return redirect(url_for('index.index'))
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index.index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please use a different email.', 'error')
            return redirect(url_for('register'))
        user = User(username=request.form['username'], email=email, is_admin=False)
        user.set_password(request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html')
=======
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
>>>>>>> 4030101f55c1ee59ee26e71b73bb56b575fc754b
