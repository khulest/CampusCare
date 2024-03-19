import select
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    campus = db.Column(db.String(100), nullable=False)
    issue_type = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    building_block = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # Correct the relationship property name
    user = db.relationship("User", back_populates="reports")
    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100))
    gender = db.Column(db.String(100))
    student_number = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(100), nullable=False)
    institution = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    
    # Correct the relationship property name
    reports = db.relationship('Report', back_populates='user')



    