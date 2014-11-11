"""
    app.rec_down
    ~~~~~~~~~~~~
"""

from flask import Blueprint

rec_downloader_bp = Blueprint('rec_downloader', __name__)

from . import views