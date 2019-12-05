
#from flask import url_for
from app import db


class Task(db.Model):

    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))


class Appointment(db.Model):
    appointment_id = db.Column(db.Integer, primary_key=True)
    appointment_title = db.Column(db.String(128), index=True)
    appointment_status = db.Column(db.String(128))
    appointment_date = db.Column(db.Date, index=True)
    start_time = db.Column(db.Time, index=True)
    duration = db.Column(db.Time, index=True)#?
    location = db.Column(db.String(128), index=True)#customer address
    customer_name = db.Column(db.String(128), index=True)
    notes = db.Column(db.String(128), index=True)

