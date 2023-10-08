from flask import render_template
from app import app

@app.route('/job_visual')
def job_visual():
    return render_template('job_visual.html')