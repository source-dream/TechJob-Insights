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
    jobname = db.Column(db.String(120), index=True)
    jobconpany = db.Column(db.String(120), index=True)
    jobcity = db.Column(db.String(120), index=True)
    jobrequire = db.Column(db.String(240), index=True)
    jobwage = db.Column(db.String(240), index=True)
    joburl = db.Column(db.String(240), index=True)
