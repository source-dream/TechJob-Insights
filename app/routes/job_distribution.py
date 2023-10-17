from flask import render_template
from app import app

@app.route('/job_distribution')
def job_distribution():

    return render_template('job_distribution.html')