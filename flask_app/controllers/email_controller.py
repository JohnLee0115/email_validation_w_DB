from flask_app import app
from flask import render_template, request, redirect, session

from flask_app.models.email_model import Email

@app.route('/')
def email_form():

    return render_template('index.html')


@app.route('/process', methods = ['POST'])
def process_form():

    if not Email.validate_email(request.form):

        return redirect('/')

    Email.add_email(request.form)

    return redirect('/success')


@app.route('/success')
def show_success():

    all_email = Email.get_all()

    return render_template('success.html', all_email = all_email )