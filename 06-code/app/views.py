from flask import render_template, redirect, url_for, flash
from app import app, db
from datetime import datetime
from app.forms import LoginForm, RegistrationForm, AddStudentForm, BorrowForm,QueryForm,QueryResult,ReturnForm
from app.models import Student, Loan


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/datetime')
def date_time():
    now = datetime.now()
    return render_template('datetime.html', title='Date & Time', now=now)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login for {form.username.data}', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Registration for {form.username.data} received', 'success')
        return redirect(url_for('index'))
    return render_template('registration.html', title='Register', form=form)


@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    form = AddStudentForm()
    if form.validate_on_submit():
        new_student = Student(username=form.username.data, firstname=form.firstname.data,
                              lastname=form.lastname.data, email=form.email.data)
        db.session.add(new_student)
        try:
            db.session.commit()
            flash(f'New Student added: {form.username.data} received', 'success')
            return redirect(url_for('index'))
        except:
            db.session.rollback()
            if Student.query.filter_by(username=form.username.data).first():
                form.username.errors.append('This username is already taken. Please choose another')
            if Student.query.filter_by(email=form.email.data).first():
                form.email.errors.append('This email address is already registered. Please choose another')
    return render_template('add_student.html', title='Add Student', form=form)


@app.route('/borrow', methods=['GET', 'POST'])
def borrow():
    form = BorrowForm()
    if form.validate_on_submit():
        new_loan = Loan(device_id=form.device_id.data,
                        student_id=form.student_id.data,
                        borrowdatetime=datetime.now())

        db.session.add(new_loan)
        try:
            db.session.commit()
            flash(f'New Loan added', 'success')
            return redirect(url_for('index'))
        except:
            db.session.rollback()
    return render_template('borrow.html', title='Borrow', form=form)

@app.route('/report', methods=['GET', 'POST'])
def report():
    form = QueryForm()
    result = None
    if form.validate_on_submit():
        option = form.select_option.data
        id_input = form.id_input.data
        if option == 'student':
            student = Student.query.get(id_input)
            if student:
                loans = Loan.query.filter_by(student_id=id_input).all()
                result = QueryResult(student=student, loans=loans)
            else:
                flash('Student not found', 'error')
                return redirect(url_for('report'))
        elif option == 'device':
            loans = Loan.query.filter_by(device_id=id_input).all()
            if loans:
                result = QueryResult(loans=loans)
            else:
                flash('Device not found', 'error')
                return redirect(url_for('report'))
    return render_template('report.html', form=form, result=result)

@app.route('/return_book', methods=['GET', 'POST'])
def return_book():
    form = ReturnForm()
    if form.validate_on_submit():
        loan_record = Loan.query.filter_by(student_id=form.student_id.data).first()
        if loan_record:
            loan_record.returndatetime = datetime.now()
            loan_record.calculate_fine()  # Calculate fine
            db.session.commit()
            flash('Book returned successfully', 'success')
            return redirect(url_for('index'))
        else:
            flash('No book borrowed by this user', 'error')
            return redirect(url_for('return_book'))
    return render_template('return.html', title='Returning', form=form)

@app.route('/all_students', methods=['GET', 'POST'])
def all_students():
    students = Student.query.all()
    return render_template('all_students.html', title='all_students', students=students)

