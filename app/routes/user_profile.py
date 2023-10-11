<<<<<<< HEAD
from flask import render_template, redirect, url_for
from flask_login import current_user
from app import app

@app.route('/user_profile')
def user_profile():
    if current_user.is_authenticated:
        return render_template('user_profile.html')
    else:
        return redirect(url_for('login'))
=======
from flask import render_template, session
from app import app
from app.models import User


@app.route('/user_profile')
def user_profile():
    user_id = session.get('user_id')
    user = None  # 默认情况下将user设置为None
    if user_id:
        user = User.query.get(user_id)

    return render_template('user_profile.html', user=user)
>>>>>>> 4030101f55c1ee59ee26e71b73bb56b575fc754b
