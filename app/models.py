from app import db
<<<<<<< HEAD
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

class User(UserMixin, db.Model):
=======

class User(db.Model):
>>>>>>> 4030101f55c1ee59ee26e71b73bb56b575fc754b
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(64), index=True, unique=True)
<<<<<<< HEAD
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(120), index=True)
    job_name = db.Column(db.String(120), index=True)
    city = db.Column(db.String(120), index=True)
    wage = db.Column(db.String(20), index=True)
    requirements = db.Column(db.String(240), index=True)
    education = db.Column(db.String(240), index=True)
    recruiter = db.Column(db.String(240), index=True)
    company = db.Column(db.String(120), index=True)
    require = db.Column(db.String(120), index=True)
    skill = db.Column(db.String(120), index=True)
    welfare = db.Column(db.String(120), index=True)
    url = db.Column(db.String(240), index=True)

    def __repr__(self):
        return f'<Job {self.job_name}>'

class PageVisit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)  # 添加时间戳字段
    count = db.Column(db.Integer, default=0)
=======

    def __repr__(self):
        return f'<User {self.username}>'

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jobname = db.Column(db.String(120), index=True)
    jobconpany = db.Column(db.String(120), index=True)
    jobcity = db.Column(db.String(120), index=True)
    jobrequire = db.Column(db.String(240), index=True)
    jobwage = db.Column(db.String(240), index=True)
    joburl = db.Column(db.String(240), index=True)
>>>>>>> 4030101f55c1ee59ee26e71b73bb56b575fc754b
