
#from flask import url_for
from app import db


class Task(db.Model):

    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True)
    address = db.Column(db.String(128), index=True)


class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True)
    date = db.Column(db.Date, index=True)
    start_time = db.Column(db.Time, index=True)
    end_time = db.Column(db.Time, index=True)
    duration = db.Column(db.Time, index=True)#?
    location = db.Column(db.String(128), db.ForeignKey('customer.address'))#customer address
    customer_name = db.Column(db.String(128), db.ForeignKey('customer.name'))
    notes = db.Column(db.String(128), index=True)

