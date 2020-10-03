import os

from flask import Flask, render_template, request, flash, redirect, session, g, jsonify
# from forms import #FORMS GO HERE
# from models import #MODELS GO HERE

app = Flask(__name__)

# app.configs below here


@app.route('/')
def landing_page():
    """Beginning page, """
    return 'working'

@app.route('/login')
def login_page():
    """Logins a user, differentiate between admin & nonadmin"""

@app.route('/register')
def register_page():
    """Register a user regular"""

@app.route('/register/admin')
def register_admin():
    """Register an admin, maybe add a password to log in here?"""

@app.route('/quiz', methods=['GET','POST'])
def quiz():
    """Show user a quiz(forms) and let them submit"""

@app.route('/results')
def results():
    """Shows the user his results, and a score(use separate file to
       evalutate it)
    """

# @app.route('/resources')

# @app.route('/applications', methods=['GET','POST'])

# @app.route('/account')

# @app.route('/account/edit')

# @app.route('/admin')

# @app.route('/admin/edit')

# @app.route('/signout')