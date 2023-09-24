# app/routes/main.py
from flask import Blueprint, render_template, redirect, url_for
from app.Scraper.scraper import run

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/scrape_jobs')
def scrape_jobs():
    run()
    return redirect(url_for('main.index'))
