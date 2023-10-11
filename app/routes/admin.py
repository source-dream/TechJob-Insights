from flask import render_template, redirect, url_for, jsonify
from . import admin_bp
from flask_login import current_user
from app.models import User, Job, PageVisit
from app import db
import pandas as pd
from datetime import date
import datetime
import plotly.express as px

@admin_bp.route("/")
def admin():
    if current_user.is_authenticated and current_user.is_admin:
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
    if current_user.is_authenticated and current_user.is_admin:
        return render_template('admin-data.html')
    return redirect(url_for('login'))

@admin_bp.route("/user")
def admin_user():
    if current_user.is_authenticated and current_user.is_admin:
        users = User.query.all()
        return render_template('admin-user.html', users=users)
    return redirect(url_for('login'))

@admin_bp.route('/delete_user/<int:id>', methods=['DELETE'])
def delete_user(id):
    if current_user.is_authenticated and current_user.is_admin:
        user = User.query.get(id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return jsonify({'message': 'User deleted successfully'})
        else:
            return jsonify({'message': 'User not found'}), 404