"""
    app.rec
    ~~~~~~~
"""

from flask import Blueprint

rec_start_bp = Blueprint('rec_start', __name__)

from . import views