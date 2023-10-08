from flask import Blueprint
from app import app

computer_jobs_bp = Blueprint('computer_jobs', __name__)
salary_distribution_bp = Blueprint('salary_distribution', __name__)
job_distribution_bp = Blueprint('job_distribution', __name__)
job_search_bp = Blueprint('job_search', __name__)
user_profile_bp = Blueprint('user_profile', __name__)
admin_bp = Blueprint('admin', __name__)
index_bp = Blueprint('index', __name__)
login_bp = Blueprint('login', __name__)


from . import computer_jobs, job_visual, user_profile, admin, index, login


# app.register_blueprint(computer_jobs_bp, url_prefix='/computer_jobs')
# app.register_blueprint(job_distribution_bp, url_prefix='/job_distribution')
# app.register_blueprint(job_search_bp, url_prefix='/job_search')
# app.register_blueprint(user_profile_bp, url_prefix='/user_profile')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(index_bp, url_prefix='/')
# app.register_blueprint(login_bp, url_prefix='/login')
