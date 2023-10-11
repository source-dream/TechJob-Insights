from flask import render_template, redirect, url_for
from flask_login import current_user
from app import app

@app.route('/user_profile')
def user_profile():
    if current_user.is_authenticated:
        return render_template('user_profile.html')
    else:
        return redirect(url_for('login'))