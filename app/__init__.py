from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
import secrets
from datetime import timedelta

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = secrets.token_hex(16) 
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)
login = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
from app import Identify
