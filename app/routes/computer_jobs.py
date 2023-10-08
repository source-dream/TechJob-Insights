from flask import render_template, request
from app import app, db
from app.models import Job
import random

@app.route('/computer_jobs/')
def computer_jobs():
    all_jobs = Job.query.all()
    if len(all_jobs) > 12:
        random_jobs = random.sample(all_jobs, 12)
    else:
        random_jobs = all_jobs
    return render_template('computer_jobs.html', jobs=random_jobs)