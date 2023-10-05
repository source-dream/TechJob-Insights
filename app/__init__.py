from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import secrets

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = secrets.token_hex(16) 

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
