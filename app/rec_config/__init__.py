"""
    app.rec_config
    ~~~~~~~~~~~~~~
"""

from flask import Blueprint

rec_config_bp = Blueprint('rec_config', __name__)

from . import views