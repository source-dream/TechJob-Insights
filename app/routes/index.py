from flask import render_template
from . import index_bp
# index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    return render_template('index.html')
