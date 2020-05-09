from flask import render_template, request, flash, redirect, url_for
from app.authentication.forms import RegistrationForm, LoginForm
from app.authentication import authentication
from app.authentication.models import User
from flask_login import login_user, logout_user, login_required, current_user

@authentication.route('/register', methods=['GET','POST'])
def register_user():
    if current_user.is_authenticated:
        flash('You are already logged-in')
        return redirect(url_for('main.display_books'))

    form = RegistrationForm()

    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.name.data,
            password=form.password.data
        )
        flash('Registration Successful')
        return redirect(url_for('authentication.sign_in_user'))
    return render_template('registration.html', form=form)

@authentication.route('/login', methods=['GET', 'POST'])
def sign_in_user():
    if current_user.is_authenticated:
        flash('You are already logged-in')
        return redirect(url_for('main.display_books'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if not user or not user.check_password(form.password.data):
            flash('Invalid Username or Password, Please try again.')
            return redirect(url_for('authentication.sign_in_user'))
        
        login_user(user, form.stay_loggedin.data)
        return redirected(url_for('main.display_books'))

    return render_template('login.html', form=form)

@authentication.route('/logout')
@login_required
def log_out_user():
    logout_user()
    return redirect(url_for('main.display_books'))