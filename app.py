import os

from flask import Flask, render_template, request, flash, redirect, session, g, jsonify
from scenarios import scenario1
app = Flask(__name__)

# app.configs below here

########

########################################
@app.route('/')
def landing_page():
    """Beginning page, """
    return render_template('home.html')


########################################
#Scenario pages
@app.route('/scenario')
def scenarios():
    """Shows all scenarios"""
    return 'Scenarios'

@app.route('/scenario/1')
def first_scenario():
    """Shows the first scenario"""
    return render_template('scenario1.html', scenario1=scenario1)


########################################
#Education Scenario
@app.route('/education')
def education_resources():
    """Shows educational resources"""

    return render_template('education.html')

@app.route('/education/scenario/<int:id>')
def resources_scenario_one(id):
    """Shows education specific for this particular scenario"""
    


