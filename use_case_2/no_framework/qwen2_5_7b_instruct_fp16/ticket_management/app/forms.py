from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired

class TicketForm(FlaskForm):
    category = SelectField('Category', choices=[
        ('facility_management', 'Facility Management'),
        ('technical_it', 'Technical IT'),
        ('services_complaints', 'Services Complaints')
    ], validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class MessageForm(FlaskForm):
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Send')