from flask import render_template, redirect, url_for, jsonify
from . import admin_bp
from flask_login import current_user
from app.models import User, Job, PageVisit
from app import db
from datetime import date
import plotly.express as px

def identify():
    if current_user.is_authenticated and current_user.auth == 'admin':
        return True
    else:
        return False

@admin_bp.route("/")
def admin():
    if current_user.is_authenticated and current_user.auth == 'admin':
        job_size = len(Job.query.all())
        user_size = len(User.query.all())
        visit_time = 0
        visit_time_day = 0
        hourly_visits = [0] * 24
        current_date = date.today()
        visits = PageVisit.query.all()
        for visit in visits:
            visit_time += visit.count 
            if visit.timestamp.date() == current_date:
                hour = visit.timestamp.hour
                visit_time_day += visit.count
                hourly_visits[hour] += visit.count
        fig = px.line(x=range(24), y=hourly_visits, title='当天每个小时的访问量')
        fig.update_layout(
            autosize=False,
            height=600,
            width=1280,
        )
        graph_html = fig.to_html(full_html=False, config={'displayModeBar': False})
        return render_template('admin.html',job_size=job_size, user_size=user_size, graph_html=graph_html, visit_time=visit_time, visit_time_day=visit_time_day)
    return redirect(url_for('login'))

@admin_bp.route("/data")
def admin_data():
    if current_user.is_authenticated and current_user.auth == 'admin':
        return render_template('admin-data.html')
    return redirect(url_for('login'))

@admin_bp.route("/user")
def admin_user():
    if current_user.is_authenticated and current_user.auth == 'admin':
        users = User.query.all()
        return render_template('admin-user.html', users=users)
    return redirect(url_for('login'))

# 获取信息接口
@admin_bp.route("/getinfo/")
def getinfo():
    if identify():
        user_size = len(User.query.all()) # 用户总数
        job_size = len(Job.query.all()) # 职位信息总数
        visit_time = 0
        visit_time_day = 0
        hourly_visits = [0] * 24
        current_date = date.today()
        visits = PageVisit.query.all()
        for visit in visits:
            visit_time += visit.count 
            if visit.timestamp.date() == current_date:
                hour = visit.timestamp.hour
                visit_time_day += visit.count
                hourly_visits[hour] += visit.count
        return {"user_size": user_size, "job_size": job_size, "visit_time": visit_time, "visit_time_day": visit_time_day}
    else:
        return redirect(url_for('login'))