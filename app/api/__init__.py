"""
    app.api
    ~~~~~~~

    This python package implements a Restful API (Representational State Transfer).
    Allows a client to view and edit configurations, instigate a recording, download
    recordings, view system status, start BIST... pretty much everything the user
    can do in the WebUI
"""

from flask import Blueprint
import flask_restful

rest_api_v1_bp = Blueprint('api_v1', __name__)
rest_api_v1 = flask_restful.Api(rest_api_v1_bp)

from . import recordings, configurations, download, status, bist