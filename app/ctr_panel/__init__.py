"""
    app.ctr_panel
    ~~~~~~~~~~~~~

"""

from flask import Blueprint

ctr_panel_bp = Blueprint('ctr_panel', __name__)

from . import views