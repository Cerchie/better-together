import os

from flask import Flask, render_template, request, flash, redirect, session, g, jsonify

app = Flask(__name__)

# app.configs below here

########

########################################
@app.route('/')
def landing_page():
    """Beginning page, """
    return 'Another test'


########################################
#Scenario pages
@app.route('/scenario')
def scenarios():
    """Shows all scenarios"""
    return 'Scenarios'

@app.route('/scenario/1')
def first_scenario():
    """Shows the first scenario"""


########################################
#Education Scenario
@app.route('/education')
def education_resources():
    """Shows educational resources"""

@app.route('/education/scenario/<int:id>')
def resources_scenario_one(id):
    """Shows education specific for this particular scenario"""
    


