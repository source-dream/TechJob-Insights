from flask import render_template
from app import app

@app.route('/user_profile')
def user_profile():

    return render_template('user_profile.html')