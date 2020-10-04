from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class EnterScenario(FlaskForm):
    """Add a scenario to list"""

    title = StringField('Title', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    suggestions = StringField('Suggestions(Separate by comma)', validators=[DataRequired()])
    insights = StringField('Insights(Separate by comma)', validators=[DataRequired()])

