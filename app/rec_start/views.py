"""
    app.rec_start.views
    ~~~~~~~~~~~~~~~~~~~
"""

# current package imports
from . import rec_start_bp


@rec_start_bp.route('/')
def recorder():
    """
        rec_start.recorder
        ~~~~~~~~~~~~~~~~~~
        

    """
    return "In progress"
