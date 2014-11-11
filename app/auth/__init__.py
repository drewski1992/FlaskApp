"""
    app.auth
    ~~~~~~~~

    This python package provides support for user validation and
    providing a secure web interface to log into the application

"""

from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from . import views