from flask import render_template,  redirect, url_for
from app.main import bp
from app import db
from app.main.forms import TaskForm, AppointmentForm
from app.models import Task, Appointment


# Main route of the applicaitons.
@bp.route('/', methods=['GET','POST'])
def index():
    return render_template("main/index.html")


#
#  Route for viewing and adding new tasks.
@bp.route('/todolist', methods=['GET','POST'])
def todolist():
    form = TaskForm()

    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.
        new_task = Task()
        new_task.task_desc =  form.task_desc.data
        new_task.task_status = form.task_status_completed.data

        db.session.add(new_task)
        db.session.commit()

        # Redirect to this handler - but without form submitted - gets a clear form.
        return redirect(url_for('main.todolist'))

    todo_list = db.session.query(Task).all()

    return render_template("main/todolist.html",todo_list = todo_list,form= form)


#
# Route for removing a task
@bp.route('/todolist/remove/<int:task_id>', methods=['GET','POST'])
def remove_task(task_id):

    # Query database, remove items
    Task.query.filter(Task.task_id == task_id).delete()
    db.session.commit()

    return redirect(url_for('main.todolist'))


#
# Route for editing a task

@bp.route('/todolist/edit/<int:task_id>', methods=['GET','POST'])
def edit_task(task_id):
    form = TaskForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.

        current_task = Task.query.filter_by(task_id=task_id).first_or_404()
        current_task.task_desc =  form.task_desc.data
        current_task.task_status = form.task_status_completed.data

        db.session.add(current_task)
        db.session.commit()
        # After editing, redirect to the view page.
        return redirect(url_for('main.todolist'))

    # get task for the database.
    current_task = Task.query.filter_by(task_id=task_id).first_or_404()

    # update the form model in order to populate the html form.
    form.task_desc.data =     current_task.task_desc
    form.task_status_completed.data = current_task.task_status

    return render_template("main/todolist_edit_view.html",form=form, task_id = task_id)


@bp.route('/appointment_list', methods=['GET','POST'])
def appointment_list():
    form = AppointmentForm()
    appointments = Appointment.query.all()#query through appointments
    if form.validate_on_submit():
        for x in appointments:
            if x.date == form.date.data and x.start_time == form.start_time.data: #if already appointment at that time
                return redirect(url_for(''))#?

        new_appointment = Appointment(title = form.title.data, status = form.status.data, date = form.date.data, start_time = form.start_time.data,
                                      duration = form.duration.data, location = form.location.data,
                                      customer_name = form.customer_name.data, notes = form.notes.data)

        db.session.add(new_appointment)
        db.session.commit()

        # Redirect to this handler - but without form submitted - gets a clear form.
        return redirect(url_for('main.appointment_list'))

    appointment_list = db.session.query(Appointment).all()#query through appointments#?
    return render_template("main/appointment_list.html", appointment_list=appointment_list, form=form)


@bp.route('/appointment_list/edit/<int:appointment_id>', methods=['GET','POST'])
def edit_appointment(appointment_id):
    form = AppointmentForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.

        current_appointment = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()
        current_appointment.title = form.title.data
        current_appointment.status = form.status_completed.data
        current_appointment.date = form.date.data
        current_appointment.start_time = form.start_time.data
        current_appointment.duration = form.duration.data
        current_appointment.location = form.location.data
        current_appointment.customer_name = form.customer_name.data
        current_appointment.notes = form.notes.data

        db.session.add(current_appointment)
        db.session.commit()
        # After editing, redirect to the view page.
        return redirect(url_for('main.appointment_list'))

    # get appointment for the database.
    current_appointment = Appointment.query.filter_by(appointment_id=appointment_id).first_or_404()

    # update the form model in order to populate the html form.
    form.title.data = current_appointment.title
    form.status_completed.data = current_appointment.status

    return render_template("main/appointment_list_edit_view.html", form=form, appointment_id=appointment_id)


@bp.route('/appointment_list/remove/<int:appointment_id>', methods=['GET','POST'])
def delete_appointment(appointment_id):
    # Query database, remove items
    Appointment.query.filter(Appointment.appointment_id == appointment_id).delete()
    db.session.commit()

    return redirect(url_for('main.appointment_list'))

#Change status???
