"""
    app.bist
    ~~~~~~~~

"""

from flask import Blueprint

bist_bp = Blueprint('bist', __name__)

from . import views