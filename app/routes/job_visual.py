from flask import render_template, redirect, url_for
from flask_login import current_user
from app import app

@app.route('/job_visual')
def job_visual():
    if current_user.is_authenticated:
        return render_template('job_visual.html')
    else:
        return redirect(url_for('login'))