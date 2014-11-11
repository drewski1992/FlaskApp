"""
    app.api.recordings
    ~~~~~~~~~~~~~~~~~~

    Contains Flask-Restful api resources used for handeling recording
    data.

"""

# Imports from flask.ext
import flask_restful

# Imports from app
from app.models import Recording, User, EventTag
from app import serializer

# Imports from api
from . import rest_api_v1


class RecordingList(flask_restful.Resource):
    """
        Fetches the full Recording List from the database,
        data in returned as JSON.
    """
    def get(self):
        recs = Recording.query.all()
        return serializer.RecordSerializer(recs, many=True).data


class RecordByID(flask_restful.Resource):
    """
        Fetches the Recording from the database by its ID,
        data in returned as JSON.
    """
    def get(self, rec_id):
        rec = Recording.query.filter_by(rec_id=rec_id).first()
        return serializer.RecordSerializer(rec).data


class RecordByName(flask_restful.Resource):
    """
        Fetches the Recording from the database by its name,
        data in returned as JSON.
    """
    def get(self, rec_name):
        rec = Recording.query.filter_by(rec_name=rec_name).first()
        return serializer.RecordSerializer(rec).data


class TagEventByRec(flask_restful.Resource):
    """
        Fetches all Event Tags that pertain to a certain recording,
        data is returned as JSON.
    """
    def get(self, record_id):
        tags = EventTag.query.filter_by(record_id=record_id)
        return serializer.EventTagSerializer(tags).data


# TODO This may or may not be needed... should only be used by Blade Control Process
class NewRecord(flask_restful.Resource):
    """
        Adds a new record to the data base.
    """
    def get(self, record_id):
        return 1


# TODO Add resources for starting a recording and downloading a recording

# Register restful api resources on the blueprint
rest_api_v1.add_resource(RecordingList, '/rec/list')
rest_api_v1.add_resource(RecordByID, '/rec/<int:rec_id>')
rest_api_v1.add_resource(RecordByName, '/rec/<string:rec_name>')
# TODO Fix Event Tag GET
rest_api_v1.add_resource(TagEventByRec, '/rec/tag/<int:record_id>')
