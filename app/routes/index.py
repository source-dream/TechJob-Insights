from flask import render_template
from flask_login import current_user
from . import index_bp
from app import db
from app.models import Job, User

@index_bp.route('/')
def index():
    return render_template('index.html')

@index_bp.route('/user')
def user():
    if current_user.is_authenticated and current_user.auth == 'admin':
        all_users = User.query.all()
        user_data = [{"id": user.id,"username": user.username,"email": user.email,"password": user.password,"auth": user.auth} for user in all_users]
        return {"data":user_data}

@index_bp.route('/job', methods=['POST'])
def job():
    if current_user.is_authenticated and current_user.auth == 'admin':
        all_jobs = Job.query.all()
        
        job_data_2d_list = [[job.id, job.tag,job.job_name, job.city,job.wage, job.requirements,job.education, job.recruiter,job.company, job.require,job.skill, job.welfare, job.url] for job in all_jobs]
        return {"data": job_data_2d_list}
