"""
    app.auth.views
    ~~~~~~~~~~~~~~
    Used for rendering templates that are involved with
    login and creating new users

"""

# Python2.7 Imports
import time

# Imports from flask and flask.ext
from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user

# Imports from app
from app import db
from app.models import User, Log

# Imports from auth
from .forms import LoginForm, RegistrationForm
from . import auth_bp

@auth_bp.before_request
def before_request():
    if current_user.is_authenticated():
        #current_user.ping()
        if request.endpoint[:5] != 'auth.':
            return redirect(url_for('auth.unconfirmed'))


@auth_bp.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous() or current_user.confirmed:
        redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth_bp.route('/login', methods=['GET', 'POST'])
@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        form = LoginForm(request.form)
        user = User.query.filter_by(name=form.name.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)

            # Log the User's Activity in Database
            log = Log(user_id=user.id, action="LOG_IN", date=time.time()*1000000,
                      message="User: {0} log in at {1}".format(user.name, time.ctime()),
                      level="auth")
            db.session.add(log)
            db.session.commit()

            return redirect(url_for('ctr_panel.control_panel'))
        else:
            error = 'Invalid Username or Password'
            flash('Invalid Username or Password')
    return render_template('auth/login.html', form=LoginForm(), error=error)


@auth_bp.route('/logout')
@login_required
def logout():
    user = current_user._get_current_object()
    logout_user()
    flash("You have been logged out")
    log = Log(user_id=user.id, action="LOG_OUT", date=time.time()*1000000,
              message="User: {0} log out at {1}".format(user.name, time.ctime()),
              level="auth")
    db.session.add(log)
    db.session.commit()
    return redirect(url_for('auth.login'))


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        form = RegistrationForm(request.form)

        # Add the User to the database
        user = User(name=form.name.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()

        # Update the database Log, report new user was created
        log = Log(user_id=user.id, action="REGISTER", date=time.time()*1000000,
                  message="User: {0} register at {1}".format(user.name, time.ctime()),
                  level="auth")
        db.session.add(log)
        db.session.commit()

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=RegistrationForm())
