from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, current_user
from datetime import datetime

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'mthobisi'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth
    from .models import User, Report

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    @app.route('/submit_report', methods=['POST'])
    def submit_report():
        
        date_str = request.form['date']
        date = datetime.fromisoformat(date_str)

        campus = request.form['campus']
        issue_type = request.form['issue_type']
        description = request.form['description']
        rating = int(request.form['rating'])
        building_block = request.form['building_block']
    
        # Assuming you have a current_user variable representing the logged-in user
        report = Report(date=date, campus=campus, issue_type=issue_type, description=description, rating=rating, building_block=building_block)
        db.session.add(report)
        db.session.commit()
        flash('Report submitted successfully!', 'success')
        return render_template('home.html', user=current_user)

    return app

def create_database(app):
    if not path.exists('Website/' + DB_NAME):
        with app.app_context():
            db.create_all()
            print('Created Database!')


