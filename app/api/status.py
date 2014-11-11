"""
    app.api.status
    ~~~~~~~~~~~~~~

"""

# Python2.7
import time

# flask imports
from flask import jsonify

# Imports from flask.ext
import flask_restful

# Imports from app
from app.models import ServerStatus

# Imports from api
from . import rest_api_v1


def get_status():
    """
        app.api.status.status
        ~~~~~~~~~~~~~~~~~~~~~

        Purpose of this route is to proved json to the client with the
        server's status and time periodically. Jquery functions will update the
        DOM dynamically.
    """
    status = ServerStatus.query.first()

    args = {}
    if status is not None:
        if status.executing_bit:
            args['executing_bit'] = "ON"
        else:
            args['executing_bit'] = "OFF"

        if status.recording:
            args['recording'] = 'ON'
        else:
            args['recording'] = 'OFF'

        if status.config_active:
            args['config_active'] = 'ACTIVE'
        else:
            args['config_active'] = 'INACTIVE'

        args['space_used'] = status.space_used
        args['space_fail'] = status.space_fail
        args['space_avail'] = status.space_avail
        args['opr_status'] = status.opr_status

    else:
        args['executing_bit'] = "[No Status]"
        args['recording'] = "[No Status]"
        args['config_active'] = "[No Status]"
        args['space_used'] = "[No Status]"
        args['space_avail'] = "[No Status]"
        args['space_fail'] = "[No Status]"
        args['opr_status'] = "[No Status]"

    args['sys_time'] = time.ctime()

    return jsonify(args)


class Status(flask_restful.Resource):
    """
        Returns the server's status
    """
    def get(self):
        return get_status()


rest_api_v1.add_resource(Status, '/status')
