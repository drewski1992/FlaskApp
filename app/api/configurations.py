"""
    app.api.configurations
    ~~~~~~~~~~~~~~~~~~~~~~

"""

# flask imports
from flask import request

# flask extensions
import flask_restful

# Imports from app
from app.models import User, Configuration, CurrentConfiguration
from app import serializer

# Imports from api
from . import rest_api_v1


class ConfigurationList(flask_restful.Resource):
    """
        Fetches all of the Configuration data from the database
    """
    def get(self):
        config = Configuration.query.all()
        return serializer.ConfigurationSerializer(config)


class ConfigurationByID(flask_restful.Resource):
    """
        Fetches a Configuration by its ID
    """
    def get(self, config_id):
        config = Configuration.query.filter_by(config_id=config_id).first()
        return serializer.ConfigurationSerializer(config)


class ConfigurationByName(flask_restful.Resource):
    """
        Fetches a Configuration by its Name
    """
    def get(self, config_name):
        config = Configuration.query.filter_by(config_name=config_name).first()
        return serializer.ConfigurationSerializer(config)


class AddConfiguration(flask_restful.Resource):
    """
        Adds a Configuration to the Table
    """
    def put(self):
        config = request.form.to_dict(flat=False)



rest_api_v1.add_resource(ConfigurationList, '/config/list')
rest_api_v1.add_resource(ConfigurationByID, '/config/<int:config_id>')
rest_api_v1.add_resource(ConfigurationByName, '/config/<string:config_name>')
rest_api_v1.add_resource(AddConfiguration, '/config/add')