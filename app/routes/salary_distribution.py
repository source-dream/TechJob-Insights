from flask import render_template
from app import app

@app.route('/salary_distribution')
def salary_distribution():

    return render_template('salary_distribution.html')