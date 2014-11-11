"""
    app.serializer
    ~~~~~~~~~~~~~~

    The purpose of this python module is to provide support for converting
    data from the sqlite database into json.
"""
# TODO Update fields to match tables

from marshmallow import Serializer, fields


class UserSerializer(Serializer):
    """
    """
    class Meta:
        fields = ("id", "email")


class RecordSerializer(Serializer):
    """
    """
    class Meta:
        fields = ('rec_id', 'rec_name', 'label', 'rec_size', 'start_time', 'end_time')


class EventTagSerializer(Serializer):
    """
    """
    record = fields.Nested(RecordSerializer)

    class Meta:
        fields = ('tag_id', 'description', 'tag_time', 'record_id')


class ConfigurationSerializer(Serializer):
    """
    """
    class Meta:
        fields = ('config_id', 'config_name', 'config_time')


class CurrentConfigSerializer(Serializer):
    """
    """
    configuration = fields.Nested(ConfigurationSerializer)

    class Meta:
        fields = ('current_config_id', )


class ConfigEthDetailSerializer(Serializer):
    """
    """
    configuration = fields.Nested(ConfigurationSerializer)

    class Meta:
        fields = ('detail_id', 'eth_channel', 'port', 'ip', 'type', 'config_id')
