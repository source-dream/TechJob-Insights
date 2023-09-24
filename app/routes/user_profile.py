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
