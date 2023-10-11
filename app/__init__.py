from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
<<<<<<< HEAD
from flask_login import LoginManager
import secrets
from datetime import timedelta
import pytz

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = secrets.token_hex(16) 
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)
login = LoginManager(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
# app.config['TIMEZONE'] = pytz.timezone('UTC')


from app import routes, models
from app import Identify
=======

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
>>>>>>> 4030101f55c1ee59ee26e71b73bb56b575fc754b
