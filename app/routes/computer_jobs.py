<<<<<<< HEAD
from flask import render_template, url_for, redirect
from flask_login import current_user
from app import app, db
from app.models import Job
import random

@app.route('/computer_jobs/')
def computer_jobs():
    if current_user.is_authenticated:
        all_jobs = Job.query.all()
        if len(all_jobs) > 12:
            random_jobs = random.sample(all_jobs, 12)
        else:
            random_jobs = all_jobs
        return render_template('computer_jobs.html', jobs=random_jobs)
    else:
        return redirect(url_for('login'))
    
=======
from flask import render_template
from app import app

@app.route('/computer_jobs')
def computer_jobs():

    return render_template('computer_jobs.html')
>>>>>>> 4030101f55c1ee59ee26e71b73bb56b575fc754b
