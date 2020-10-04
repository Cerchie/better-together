import os

from flask import Flask, render_template, request, flash, redirect, session, g, jsonify
from forms import EnterScenario
from scenarios import scenario1, MAIN_LIST, create_scenario, get_scenarios
import pdb
app = Flask(__name__)

# app.configs below here
app.config['SECRET_KEY'] = 'tardigrades'
########
@app.before_request
def session_set():
    check_session()

def check_session():
    if 'scenarios' not in session:
        session['scenarios'] = [MAIN_LIST[0], MAIN_LIST[1], MAIN_LIST[2]]

########################################
@app.route('/')
def landing_page():
    """Beginning page, """
    return render_template('home.html')


########################################
#Scenario pages
@app.route('/scenario')
def scenario_list():
    """Shows all scenarios, Uses session to store each scenario the user makes"""

    list_of_scenarios = session['scenarios']
    
    return render_template('scenario_list.html', scenarios=list_of_scenarios)

@app.route('/scenario/<int:number>')
def scenarios(number):
    """Shows the first scenario"""
    for item in session['scenarios']:
        if item['id'] == number:
            return render_template('scenario.html', scenario=item)

########################################
#Education Scenario
@app.route('/education')
def education_resources():
    """Shows educational resources"""

    return render_template('education.html')

@app.route('/education/scenario/<int:id>')
def resources_scenario_one(id):
    """Shows education specific for this particular scenario"""
    

@app.route('/scenario_maker', methods=['GET','POST'])
def make_scenario():
    """Let user create their own scenarios"""
    form = EnterScenario()

    if form.validate_on_submit():
        new_scenario = create_scenario(form.title.data, form.description.data, form.suggestions.data, form.insights.data)
        session['scenarios'].append(new_scenario)
        session.modified = True
        return redirect('/scenario')
    else:
        flash(f'Something went wrong!','danger')

    return render_template('create_scenario.html', form = form)


@app.errorhandler(404)
def page_not_found(err):
    """Page non existent"""

    return render_template('404.html'), 404