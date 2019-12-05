
# import flask_wtf
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from wtforms import DateField, TimeField



class TaskForm(FlaskForm):
    task_desc = StringField('task_desc', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo','Todo'),('doing','Doing'),('done','Done')])

    submit = SubmitField('submit')


class AppointmentForm(FlaskForm):
    appointment_title = StringField('Title: ', validators=[DataRequired()])
    appointment_status_completed = SelectField('Status: ', choices=[('todo', 'Todo'), ('doing', 'Doing'), ('done', 'Done')])
    appointment_date = DateField('Date (year-month-date): ', validators=[DataRequired()])
    start_time = TimeField('Start time: ', validators=[DataRequired()])
    duration = TimeField('Duration: ', validators=[DataRequired()])
    location = StringField('Location (Customer address): ', validators=[DataRequired()])#customer address
    customer_name = StringField('Customer name: ', validators=[DataRequired()])
    notes = StringField('Notes: ')

    submit = SubmitField('Submit')
