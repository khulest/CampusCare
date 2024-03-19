from flask import Blueprint, app, render_template, request
from flask_login import login_required,current_user

from website import DB_NAME
from .models import Report 


# Define the blueprint
views = Blueprint('views', __name__)


# Define the route for rendering the home template
@views.route('/')
@login_required
def home():
    data = Report.query.all()
    # Render the home.html template from the 'templates' directory
    return render_template("home.html",user=current_user,data=data)

@views.route('/about_Us')

def about_Us():
    # Render the home.html template from the 'templates' directory
    return render_template("about_Us.html")


@views.route('/admin', methods=['GET', 'POST'])
@login_required

def admin():
    data = Report.query.all()
    # Check if the user is an admin
    if current_user.is_authenticated and current_user.email == "MaintananceAdmin@gmail.com":
        # User is authenticated and has admin privileges
        # Render the admin dashboard page
        data = Report.query.all()
        return render_template('admin.html',data=data)
    else:
        # User does not have admin privileges
        # Redirect to the home page or show an error message
        
     
     return render_template("home.html",data=data )



