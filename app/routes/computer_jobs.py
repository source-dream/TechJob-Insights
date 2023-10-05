from flask import render_template
from app import app

@app.route('/computer_jobs')
def computer_jobs():
    return render_template('computer_jobs.html')