from flask import render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import LoginForm, RegistrationForm, AccountForm
from app.models import load_model, predict

model, tokenizer = load_model()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')



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

@app.route('/account', methods=['GET', 'POST'])
def account():
    form = AccountForm()
    if form.validate_on_submit():

        account_text = form.account.data
        # Use the model to get the prediction
        prediction_label = predict(model, tokenizer, account_text)
        # Redirect to the same page with the prediction result
        return render_template('account.html', title='Classification', form=form, prediction=prediction_label)
    
    return render_template('account.html', title='Classification', form=form)


