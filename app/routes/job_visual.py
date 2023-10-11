from flask import render_template, redirect, url_for
from flask_login import current_user
from app import app
import app.others.data_processing as dp

@app.route('/job_visual')
def job_visual():
    if current_user.is_authenticated:
        #学历要求
        education_data=dp.education_wanted()
        worldcloud_data=dp.welfare()
        experience_data=dp.experience_wanted()
        job_data=dp.job_info()
        city_data=dp.city_distribution()
        return render_template('job_visual.html',education_data=education_data,worldcloud_data=worldcloud_data,
                               experience_data=experience_data,job_data=job_data,city_data=city_data)
    else:
        return redirect(url_for('login'))

