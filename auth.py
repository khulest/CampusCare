from flask import Blueprint, render_template, request, flash ,redirect,url_for
from werkzeug.security import generate_password_hash,check_password_hash
from . models import User
from . import db
from flask_login import login_user,login_required,logout_user,current_user
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST']) 
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()  
        if user:  
            if check_password_hash(user.password, password): 
                flash('Logged in successfully!', category='success')
                login_user(user,remember=True)
                return redirect(url_for('views.home'))  
            else:
                flash('Incorrect password. Please try again.', category='error')
        else:
            flash('Email does not exist. Please sign up.', category='error')

    return render_template("login.html",user=current_user)

@auth.route('/logout') 
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST']) 
def sign_up():
    if request.method == 'POST':
        # Get form data
        firstName = request.form.get('firstName')
        Surname = request.form.get('Surname')
        gender = request.form.get('gender')
        student_number = request.form.get('student_number')
        phone_number = request.form.get('phone_number')
        institution = request.form.get('institution')
        email = request.form.get('email')
        password = request.form.get('password')
        

        # Validate form data
        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(Surname) < 2:
            flash('Surname must be greater than 1 character.', category='error')
        elif not gender:
            flash('Please select your gender.', category='error')
        elif not institution:
            flash('Please select your institution.', category='error')
        elif password != password:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
          
            hashed_password= generate_password_hash(password, method='pbkdf2:sha256')
            
            
            new_user = User(email=email, firstName=firstName, surname=Surname, gender=gender, 
                            password=hashed_password, 
                            student_number=student_number, phone_number=phone_number,
                            institution=institution)

            db.session.add(new_user)

            db.session.commit()
            login_user(new_user,remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html",user=current_user)