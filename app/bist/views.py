"""
    app.bist.views
    ~~~~~~~~~~~~~~

"""

from . import bist_bp

@bist_bp.route('/')
def bist():
	return "In Progess"
