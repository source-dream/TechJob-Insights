from flask import render_template
from app import app

@app.route('/job_search')
def job_search():

    return render_template('job_search.html')