from flask import render_template, request, url_for, flash, redirect
from werkzeug.security import generate_password_hash, check_password_hash
from app import app, db
from app.models import User

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the email exists in the database
        user = User.query.filter_by(username=username).first()
        if user is None:
            user = User.query.filter_by(email=username).first()
            if user is None:
                flash('Invalid email or password', 'error')
                return redirect(url_for('login'))

        # Check if the password is correct
        if not check_password_hash(user.password, password):
            flash('Invalid email or password', 'error')
            return redirect(url_for('login'))
        
        # Check if the user has been verified via email (you may need to update your User model)
        # if not user.is_verified:
        #     flash('Your email has not been verified. Please check your email for a verification code.', 'error')
        #     return redirect(url_for('login'))

        # Log in the user (you may need to implement a session-based authentication system)
        # For example, you can use Flask-Login for session management.

        flash('Login successful', 'success')
        return redirect(url_for('index.index'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # 检查邮箱是否已被使用
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please use a different email.', 'error')
            return redirect(url_for('register'))

        # Create a new user
        new_user = User(username=username, email=email, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html')