from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return f'<User {self.username}>'

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(120), index=True)
    company = db.Column(db.String(120), index=True)
    city = db.Column(db.String(120), index=True)
    requirements = db.Column(db.String(240), index=True)
    wage = db.Column(db.String(20), index=True)
    url = db.Column(db.String(240), index=True)

    def __repr__(self):
        return f'<Job {self.job_name}>'
